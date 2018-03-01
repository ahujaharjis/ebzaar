from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from datetime import timedelta
from xlrd import open_workbook
from xlutils.copy import copy
import csv
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import *
import os
# Create your views here.


def home(request,epids={},eskus={},esmrps={}):
    form = ResultsForm()
    return render(request,'mapping/home.html',{'form':form,'epids':epids,'eskus':eskus,'esmrps':esmrps})

def modify_base_file(path1,path2):
    ebzar_name = []
    ebzar_sku = []
    ebzar_mrp = []
    ebzar_sp = []
    skip = True
    with open(path2) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if skip:
                skip = False
            else:
                ebzar_name.append(row[2])
                ebzar_sku.append(int(row[0]))
                ebzar_mrp.append(row[4])
                ebzar_sp.append(row[6])

    rb = open_workbook(path1)
    r_sheet = rb.sheet_by_index(0)  # read only copy to introspect the file
    wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
    w_sheet = wb.get_sheet(0)  # the sheet to write to within the writable copy
    START_ROW = 0
    for row_index in range(START_ROW, r_sheet.nrows):
        sku = r_sheet.cell(row_index, 2).value
        if sku in ebzar_sku:
            i = ebzar_sku.index(sku)
            if ebzar_sp[i] == '':
                w_sheet.write(row_index, 5, ebzar_mrp[i])
            else:
                w_sheet.write(row_index, 5, ebzar_sp[i])

            w_sheet.write(row_index, 4, ebzar_mrp[i])

    wb.save(path1)

def get_changes(request,path1,path2,path3,path4):
    seller_id = []
    seller_product_name = []
    seller_old_mrp = []
    seller_old_sp = []
    base_id = []
    base_product_name = []
    base_sku = []
    base_old_mrp = []
    base_ebazr_name = []
    base_old_sp = []
    base_status = []
    base_date = []
    ebzr_sku = []
    ebzr_date = []
    ebzr_quant = []
    ebzr_name = []
    esmrps = []
    skip = True
    with open(path3) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if skip:
                skip = False
            else:
                try:
                    seller_old_sp.append(float(row[2]))
                    seller_old_mrp.append(float(row[3]))
                    item = row[0]
                    if int(item) in seller_id:
                        index = seller_id.index(int(item))
                        if row[3] > seller_old_mrp[index]:
                            seller_old_mrp[index] = row[3]
                            seller_old_sp[index] = row[2]
                    else:
                        seller_id.append(int(row[0]))
                        seller_product_name.append(row[1])


                except ValueError:
                    esmrps.append(row[1])

    skip = True
    with open(path2) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if skip:
                skip = False
            else:
                ebzr_name.append(row[2])
                ebzr_sku.append(int(row[0]))
                ebzr_date.append(row[8])
                ebzr_quant.append(int(row[5]))

    book = open_workbook(path1, on_demand=True)
    sheet = book.sheet_by_name('Sheet1')
    pids = []
    epids = []
    skus = []
    eskus = []
    skip = True
    for row in range(sheet.nrows):
        if skip:
            skip = False
        else:
            item = sheet.cell(row, 0).value
            if item in pids:
                print('duplicate pids', int(item), sheet.cell(row, 1).value)
                epids.append(int(item))
            else:
                pids.append(item)
            base_id.append(sheet.cell(row, 0).value)
            base_product_name.append(sheet.cell(row, 1).value)
            item = sheet.cell(row, 2).value
            if item in skus:
                print('duplicate skus', int(item), sheet.cell(row, 1).value)
                eskus.append(int(item))
            else:
                skus.append(item)
            base_sku.append(sheet.cell(row, 2).value)
            base_ebazr_name.append(sheet.cell(row, 3).value)
            base_old_mrp.append(sheet.cell(row, 4).value)
            base_old_sp.append(sheet.cell(row, 5).value)
            base_status.append(int(sheet.cell(row, 6).value))

    if epids or eskus or esmrps:
        return home(request,epids,eskus,esmrps)
    with open(path4, 'w') as out_csv:

        writer = csv.writer(out_csv, delimiter=',', lineterminator='\n')
        row = ['Sku', 'Ean', 'Name', 'Status', 'Price', 'Quantity', 'Special:Price', 'Special:Date Start',
               'Special:Date End']
        writer.writerow(row)
        for item in ebzr_sku:
            ind = ebzr_sku.index(item)
            quant = ebzr_quant[ind]
            date = datetime.date.today() + timedelta(days=30)

            if item in base_sku:
                index = base_sku.index(item)
                val = base_id[index]

                if val in seller_id and index != 0:
                    i = seller_id.index(val)

                    d = float(seller_old_mrp[i]) - float(seller_old_sp[i])

                    if base_status[index] == 0:

                        if d > 0:
                            dateini = datetime.date.today()
                            dateend = date
                            s = seller_old_sp[i]
                        else:
                            dateini = ''
                            dateend = ''
                            s = ''
                        row = [base_sku[index], '', base_ebazr_name[index], '1', seller_old_mrp[i], '100', s, dateini,
                               dateend]
                        writer.writerow(row)

                    elif (float(base_old_mrp[index]) != float(seller_old_mrp[i])) or (float(base_old_sp[index]) != float(seller_old_sp[i])):
                        if d > 0:
                            dateini = datetime.date.today()
                            dateend = date
                            s = seller_old_sp[i]
                        else:
                            dateini = ''
                            dateend = ''
                            s = ''
                        row = [base_sku[index], '', base_ebazr_name[index], '1', seller_old_mrp[i], '100', s, dateini,dateend]

                        writer.writerow(row)
                    else:
                        pass


                else:

                    if index != 0 and not base_old_mrp[index].startswith('9999'):
                        row = [base_sku[index], '', base_ebazr_name[index], '0', '9999', '0', '', '', '']
                        writer.writerow(row)
            else:
                pass

    with open(path4, 'rb') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=SellerProductList-'+str(datetime.date.today().strftime("%Y%m%d"))+'_SS_Update.csv'
        return response

def results(request):
    if request.method == 'POST':
        path = os.path.dirname(os.path.dirname(__file__))
        for f in os.listdir(path):
            if f.endswith("basefile.csv") or f.endswith("vendorfile.csv") or f.endswith("ebazrfile.csv") or f.endswith("final.csv"):
                os.remove(f)
        form = ResultsForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            base_file = request.FILES['base_file']
            vendor_file = request.FILES['vendor_file']
            ebazr_file = request.FILES['ebazr_file']
            result_file = request.FILES['ebazr_file']


            path1 = default_storage.save('basefile.csv', ContentFile(base_file.read()))
            path2 = default_storage.save('ebazrfile.csv',ContentFile(ebazr_file.read()))
            path3 = default_storage.save('vendorfile.csv',ContentFile(vendor_file.read()))
            path4 = default_storage.save('final.csv',ContentFile(result_file.read()))

            modify_base_file(path1, path2)
            return get_changes(request,path1,path2,path3,path4)


        else:
            return HttpResponse('not valid')

