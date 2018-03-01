from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
import datetime
from datetime import timedelta
import csv
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import *
from .models import *
import json
import os
import io
import zipfile
from io import BytesIO
from django.template.loader import get_template
from decimal import *
from xhtml2pdf import pisa
from num2words import num2words

# Create your views here.
def calculation(dmin,dmax):
    print(dmin,dmax)
    order_ids = []
    merchant_names = []
    prices = []
    order_dates = []
    paymentmodes = []
    productprices = []
    orders = OcOrder.objects.all()
    for order in orders:
        if datetime.datetime.strptime(dmin, "%Y-%m-%d").date() <= order.date_added.date() and order.date_added.date() <= datetime.datetime.strptime(dmax, "%Y-%m-%d").date() and order.order_status_id==5:
            order_id = order.order_id

            if OcCustomerpartnerToOrder.objects.filter(order_id=order_id).exists():
                custpart_obj = OcCustomerpartnerToOrder.objects.filter(order_id=order_id)[0]
                customer_id = custpart_obj.customer_id

                if OcCustomerpartnerToStorelocator.objects.filter(customer_id=customer_id).exists():
                    store= OcCustomerpartnerToStorelocator.objects.filter(customer_id=customer_id)[0]
                    store_name = OcStorelocatorStore.objects.filter(storelocator_id=store.storelocator_id)[0]
                    sum = 0
                    order_ids.append(order_id)
                    merchant_names.append(store_name)
                    prices.append(order.total)
                    order_dates.append(order.date_added)
                    paymentmodes.append(order.payment_method)
                    products = OcOrderProduct.objects.filter(order_id=order_id)
                    for product in products:
                        sum=sum+product.total
                    productprices.append(sum)
    zipped_file = io.BytesIO()
    with zipfile.ZipFile(zipped_file, 'w') as zip:
        completed_merchants=[]
        files = []
        for name in merchant_names:
            if name not in completed_merchants:
                commission_total = 0
                price_sum = 0
                amt_sum = 0
                netpay_sum = 0
                orders = []
                objs=DefaultRate.objects.filter(store_name__store_name_backend=name)
                rate = 5
                tax_inclusive = False
                pgpass = False
                reimbursements = Reimbursement.objects.filter(store_name__store_name_backend=name)
                reimburse_orders = []
                thresamt = 0
                amt = 0
                promos = Promo.objects.filter(store_name__store_name_backend=name)
                promos_orders = []
                promos_rates = []
                promo_lists = []
                promos_skus = []
                promos_price = []
                conc_perorder = ConcessionalRate.objects.filter(store_name__store_name_backend=name).filter(Q(type='FLAT PER ORDER') | Q(type='PERCENTAGE'))
                type = ''
                conc_rate = 0
                conc_orders = []
                conc_prices = []
                conc_totals = []
                conc_persku = ConcessionalRate.objects.filter(store_name__store_name_backend=name,type='FLAT PER SKU',date_from__lte=datetime.date.today()).filter(Q(date_to__isnull=True) | Q(date_to__gte=datetime.date.today()))

                conc_skus = []
                conc_skuorders = []
                conc_skurates = []
                conc_sku = []
                conc_price = []
                for c_sku in conc_persku:
                    conc_skus.append(c_sku.sku.sku)

                conc_percateogry = ConcessionalRate.objects.filter(store_name__store_name_backend=name,type='RATE PER CATEGORY',date_from__lte=datetime.date.today()).filter(Q(date_to__isnull=True) | Q(date_to__gte=datetime.date.today()))
                conc_cat_products_rate = []
                conc_cat_products = []
                for conc_cat in conc_percateogry:

                    categories = OcCategory.objects.filter(Q(parent_id=conc_cat.category_id)|Q(category_id=conc_cat.category_id))

                    for cat in categories:

                        prod_cat = OcProductToCategory.objects.filter(category_id=cat.category_id)

                        for obj in prod_cat:
                            object = OcProduct.objects.filter(product_id=obj.product_id)[0]

                            conc_cat_products.append(object)
                            conc_cat_products_rate.append(conc_cat.rate)
                c_orders = []
                c_products = []
                c_totals = []
                c_rates = []
                zones = DeliveryZone.objects.filter(store_name__store_name_backend=name,delivered_by='EBAZR',date_from__lte=datetime.date.today()).filter(Q(date_to__isnull=True) | Q(date_to__gte=datetime.date.today()))
                zones_pincodes = []
                zone_orders = []
                zone_prices = []
                for zone in zones:
                    zones_pincodes.append(zone.pincodes)
                delivery_rate = 5
                if zones:
                    delivery_rate_obj = AdditionalCommRate.objects.filter(store_name__store_name_backend=name,date_from__lte=datetime.date.today()).filter(Q(date_to__isnull=True) | Q(date_to__gte=datetime.date.today()))[0]
                    delivery_rate = delivery_rate_obj.rate

                cancelled_orders = Penalty_orders.objects.filter(store_name__store_name_backend=name,reason='Cancelled By Store')
                print(cancelled_orders)

                penalty_rate = 5
                penalty_price = 0
                penalty_obj = Penalty.objects.filter(store_name__store_name_backend=name,date_from__lte=datetime.date.today()).filter(Q(date_to__isnull=True) | Q(date_to__gte=datetime.date.today())).last()
                if penalty_obj:
                    penalty_rate = penalty_obj.orders
                    penalty_price = penalty_obj.price
                for obj in conc_perorder:
                    if obj and (obj.date_from <= datetime.date.today() and (obj.date_to == None or obj.date_to >= datetime.date.today())):
                        type = obj.type
                        conc_rate =obj.rate

                for obj in reimbursements:
                    if obj and (obj.date_from<=datetime.date.today() and (obj.date_to == None or obj.date_to>=datetime.date.today())):
                        thresamt = obj.thres_amt
                        amt = obj.amt

                for obj in objs:
                    if obj and (obj.date_from<=datetime.date.today() and (obj.date_to == None or obj.date_to>=datetime.date.today())):
                        rate = obj.rate
                        tax_inclusive = obj.tax_inclusive
                        pgpass = obj.payment_gateway_pass

                for promo in promos:
                    promo_lists.append(promo.sku.sku)

                with open(str(name) + '.csv', 'w') as out_csv:
                    writer = csv.writer(out_csv, delimiter=',', lineterminator='\n')
                    row = ['Order No', 'Order Date', 'Payment Mode', 'Total Value', 'Commission Rate%', 'Commission Amount']
                    writer.writerow(row)
                    for order in order_ids:
                        index = order_ids.index(order)
                        if merchant_names[index] == name:
                            print(name)
                            orders.append(order_ids[index])
                            price_sum = price_sum + prices[index]
                            amt_sum = amt_sum + (rate * prices[index] / 100)
                            if paymentmodes[index] != 'Cash On Delivery':
                                netpay_sum = netpay_sum + prices[index]
                                print(order_ids[index],"here")
                            row = [order_ids[index], order_dates[index], paymentmodes[index], prices[index], rate,(rate * prices[index] / 100)]
                            writer.writerow(row)
                            commission_total = amt_sum + Decimal(netpay_sum*1.0/100)

                            if amt and thresamt:
                                if productprices[index]<thresamt:
                                    reimburse_orders.append(order_ids[index])

                            if conc_cat_products:
                                products = OcOrderProduct.objects.filter(order_id=order_ids[index])
                                for product in products:
                                    obj = OcProduct.objects.filter(product_id=product.product_id).last()

                                    if obj in conc_cat_products:

                                        ind = conc_cat_products.index(obj)
                                        c_orders.append(order_ids[index])
                                        c_products.append(obj.sku)
                                        c_totals.append(product.total)

                                        c_rates.append(conc_cat_products_rate[ind])


                            if promos:
                                products = OcOrderProduct.objects.filter(order_id=order_ids[index])
                                for product in products:
                                    product_sku = OcProduct.objects.filter(product_id=product.product_id)[0]
                                    if product_sku.sku in promo_lists:

                                        promo_obj = Promo.objects.filter(store_name__store_name_backend=name,sku=product_sku,date_from__lte=datetime.date.today()).filter(Q(date_to__gte=datetime.date.today()) | Q(date_to__isnull=True)).last()
                                        if promo_obj:
                                            promos_orders.append(order_ids[index])
                                            promos_rates.append(promo_obj.rate)
                                            promos_skus.append(product_sku.sku)
                                            promos_price.append(product.total)
                            if conc_persku:
                                products = OcOrderProduct.objects.filter(order_id=order_ids[index])
                                for product in products:
                                    product_sku = OcProduct.objects.filter(product_id=product.product_id)[0]
                                    if product_sku.sku in conc_skus:
                                        conc_obj = ConcessionalRate.objects.filter(store_name__store_name_backend=name,sku=product_sku,date_from__lte=datetime.date.today()).filter(Q(date_to__gte=datetime.date.today()) | Q(date_to__isnull=True)).last()

                                        if conc_obj:
                                            conc_skuorders.append(order_ids[index])
                                            conc_skurates.append(conc_obj.rate)
                                            conc_sku.append(product_sku.sku)
                                            conc_price.append(product.total)

                            if type and conc_rate:
                                if type == 'FLAT PER ORDER':
                                    conc_orders.append(order_ids[index])
                                    conc_prices.append(prices[index])
                                    conc_totals.append(prices[index]-conc_rate)

                                elif type == 'PERCENTAGE':
                                    conc_orders.append(order_ids[index])
                                    conc_prices.append(prices[index])
                                    conc_totals.append((prices[index]*conc_rate/100))

                            if zones:
                                order_obj = OcOrder.objects.filter(order_id=order_ids[index])[0]
                                if order_obj.shipping_postcode in zones_pincodes:
                                    zone_orders.append(order_ids[index])
                                    zone_prices.append(prices[index])

                    row = []
                    writer.writerow(row)
                    writer.writerow(row)
                    row = ['', '', '', price_sum, '', amt_sum]
                    writer.writerow(row)
                    row = ['Sr No.', '', 'Details', 'Amount', '', 'TCS-1% AMT', '']
                    writer.writerow(row)
                    row = ['1', '','Total value of sales where eBZaar received payment online on behalf of Store during period' + dmin + '  to ' + dmax,
                    netpay_sum, '', (1 * netpay_sum / 100)]
                    writer.writerow(row)

                    if len(reimburse_orders)>0:
                        row = []
                        writer.writerow(row)
                        writer.writerow(row)
                        row = ['Sr No.', '', 'Details', 'Amount', '', 'REIMBURSEMENT AMOUNT', '']
                        writer.writerow(row)
                        row = ['1', '','Orders where amount is to be reimbursed '+str(reimburse_orders)+' from' + dmin + '  to ' + dmax,amt, '', len(reimburse_orders)*amt]
                        writer.writerow(row)
                        commission_total = commission_total - len(reimburse_orders)*amt

                    p_price = 0
                    if promos_orders:
                        row = []
                        writer.writerow(row)
                        writer.writerow(row)
                        row = ['Order Id', 'SKU', 'Rate', 'Product Price', 'Promo Price', '']
                        writer.writerow(row)

                        for order in promos_orders:
                            index = promos_orders.index(order)
                            row = [promos_orders[index],promos_skus[index],promos_rates[index],promos_price[index],(promos_price[index]*promos_rates[index]/100),'']
                            p_price = p_price + (promos_price[index]*promos_rates[index]/100)
                            writer.writerow(row)
                        commission_total = commission_total + p_price

                    c_price = 0
                    if conc_orders:
                        row = []
                        writer.writerow(row)
                        writer.writerow(row)
                        row = ['Order Id',type , "Rate", 'Order Total ', 'Final Price', '']
                        writer.writerow(row)

                        for order in conc_orders:
                            index = conc_orders.index(order)
                            row = [conc_orders[index], "", conc_rate, conc_prices[index],conc_totals[index], '']
                            if type == 'FLAT PER ORDER':
                                c_price = c_price + conc_rate
                            else:
                                c_price = c_price + conc_totals[index]
                            writer.writerow(row)
                        commission_total = commission_total + c_price

                    csku_price = 0
                    if conc_skuorders:
                        row = []
                        writer.writerow(row)
                        writer.writerow(row)
                        row = ['Order Id','Concessional Rate for Skus( Flat Per SKU)' ,'Rate' , 'Product Total ', ' Price', '']
                        writer.writerow(row)

                        for order in conc_skuorders:
                            index = conc_skuorders.index(order)
                            row = [conc_skuorders[index], conc_sku[index], conc_skurates[index], conc_price[index], (conc_price[index]-conc_skurates[index]), '']
                            csku_price = csku_price + conc_skurates[index]
                            writer.writerow(row)
                        commission_total = commission_total + csku_price

                    d_price = 0
                    if zone_orders:
                        row = []
                        writer.writerow(row)
                        writer.writerow(row)
                        row = ['Order Id', 'Additional Comm Charge Delivery Provided by Ebzaar', 'Rate', 'Order Total ', ' Price', '']
                        writer.writerow(row)

                        for order in zone_orders:
                            index = zone_orders.index(order)
                            row = [zone_orders[index], "", delivery_rate, zone_prices[index],(zone_prices[index] * delivery_rate / 100), '']
                            d_price = d_price + (zone_prices[index]*delivery_rate/100)
                            writer.writerow(row)
                        commission_total = commission_total + d_price

                    cat_price = 0
                    if c_products:
                        row = []
                        writer.writerow(row)
                        writer.writerow(row)
                        row = ['Order Id', 'Product By Category(SKU)', 'Rate', 'Product Total ',' Price', '']
                        writer.writerow(row)

                        for product in c_products:
                            index = c_products.index(product)
                            row = [c_orders[index], c_products[index],c_rates[index] , c_totals[index],(c_totals[index] * c_rates[index] / 100), '']
                            cat_price = cat_price + (c_totals[index]*c_rates[index]/100)
                            writer.writerow(row)
                        commission_total = commission_total + cat_price
                    penalty_prices = 0
                    if cancelled_orders:
                        print("harjis")
                        if len(cancelled_orders)>penalty_rate:

                            row = []
                            writer.writerow(row)
                            writer.writerow(row)

                            row = ['Order Id', 'Penalty for Cancellation', 'Order Total', penalty_price,'']

                            writer.writerow(row)
                            for order in cancelled_orders:
                                row = [order.order_id, "", order.price, '', '']
                                writer.writerow(row)
                            commission_total = commission_total + penalty_price
                            penalty_prices = penalty_price
                    pg_amt = 0
                    pgobjs = PgFile.objects.filter(store_name__store_name_backend=name)
                    if pgpass and pgobjs:
                        row = []
                        writer.writerow(row)
                        writer.writerow(row)
                        row = ['Order Id','Order Amount','PG Charges','PG GST','Amount to be Payed']
                        writer.writerow(row)

                        for obj in pgobjs:
                            row = [obj.order_id,obj.order_amount,obj.pg_charges,obj.pg_gst,obj.pg_charges-obj.order_amount]
                            writer.writerow(row)
                            pg_amt = pg_amt + (obj.pg_charges-obj.order_amount)

                    completed_merchants.append(name)
                    files.append(out_csv)
                zip.write(str(name)+".csv", str(name) + ".csv")
                if tax_inclusive:
                    tax=0
                else:
                    tax=round(amt_sum*18/100,2)

                word = num2words(round(commission_total+tax,2), lang='en')

                if word.find("point")!=-1:
                    word = word.replace("point", "ruppee")
                    word = word + " paise"
                else:
                    word = word +" ruppee"
                word = word + " only"

                amount=commission_total+tax

                template = get_template('commission/debit_credit_note.html')
                context = {
                    "dmin":dmin,
                    "dmax":dmax,
                    "name": name,
                    "orders":orders,
                    "amt_sum":round(amt_sum,2),
                    "netpay_sum":round(netpay_sum,2),
                    "tax":round(tax,2),
                    "commission_total": round(amount,2),
                    "reimbursement":len(reimburse_orders)*amt,
                    "promos_orders":round(p_price,2),
                    "conc_order":round(c_price,2),
                    "csku_order":round(csku_price,2),
                    "d_order":round(d_price,2),
                    "cat_order":round(cat_price,2),
                    "penalty_cancelled":round(penalty_prices,2),
                    "date":datetime.date.today(),
                    "word":word,
                }
                html = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
                if not pdf.err:
                    path = default_storage.save(str(name)+"_note.pdf", ContentFile(result.getvalue()))
                    zip.write(path, str(name) + "debit_credit_note.pdf")
                if commission_total>0:
                    template = get_template('commission/tax_invoice.html')
                    obj = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
                    total = round(amt_sum+tax,2)
                    word = num2words(total,lang='en')

                    if word.find("point"):
                        word = word.replace("point", "ruppee")
                        word = word +" paise"
                    else:
                        word = word +" ruppee"
                    word = word + " only"
                    if not tax:
                        base_amt = (amt_sum*100/118)
                        tax = (amt_sum - base_amt)/2
                        amt_sum = base_amt
                    else:
                        tax = tax/2
                    gstno = None
                    if GstStore.objects.filter(store_name__store_name_backend=name):
                        gst_obj = GstStore.objects.filter(store_name__store_name_backend=name)[0]
                        gstno = gst_obj.gstno
                    context = {
                        "date":datetime.date.today(),
                        "dmin":dmin,
                        "dmax":dmax,
                        "tax":round(tax,2),
                        "amt_sum":round(amt_sum,2),
                        "total":total,
                        "total_tax":round(tax*2,2),
                        "name":name,
                        "place":obj.store_street+" "+obj.store_city+" "+obj.store_zip,
                        "word":word,
                        "gsttinno":gstno,
                    }
                    html = template.render(context)
                    result = BytesIO()
                    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
                    if not pdf.err:
                        path = default_storage.save(str(name) + "_tax_invoice.pdf", ContentFile(result.getvalue()))
                        zip.write(path, str(name)+"tax_invoice.pdf")
        zip.close()


    response = HttpResponse(zipped_file.getvalue(), content_type = "application/x-zip-compressed")
    response['Content-Disposition'] = 'attachment; filename=comm_'+dmin+'_to_'+dmax+'.zip'
    return response

def comm_calc(request):
    if request.method == 'POST':
        path = os.path.dirname(os.path.dirname(__file__))
        for f in os.listdir(path):
            if f.endswith("_note.pdf") or f.endswith("_tax_invoice.pdf") or f.endswith("pgfile.csv"):
                os.remove(f)
        dmin = request.POST['sdate']
        dmax = request.POST['edate']
        # pgfile = request.FILES['pgfile']
        # path = default_storage.save('pgfile.csv', ContentFile(pgfile.read()))
        # skip = True
        # with open(path, encoding = "ISO-8859-1") as csvfile:
        #     reader = csv.reader(csvfile, delimiter=',')
        #     for row in reader:
        #         if skip:
        #             skip = False
        #         else:
        #             order_id = row[0]
        #             order_amount = row[1]
        #             pg_charges = row[2]
        #             pg_gst = row[3]

        return calculation(dmin,dmax)
    else:
        return render(request, 'commission/comm_base.html')


def home_commission(request):
    store = OcCustomerpartnerToStorelocator.objects.all()
    stores = []
    for s in store:
        print(s)
        obj = OcStorelocatorStore.objects.get(storelocator_id=s.storelocator_id)
        stores.append(obj.store_name_backend)
    return render(request, 'commission/home_commissiom.html', {'stores':stores})

def concessional_rate(request,name):
    if request.method == 'POST':
        formset = ConcessionalRateFormSet(request.POST)
        if formset.is_valid():
            for f in formset:
                if f .has_changed():
                    cd = f.cleaned_data
                    type = cd.get('type')
                    categories = cd.get('categories')

                    sku = cd.get('sku')
                    rate = cd.get('rate')
                    date_from = cd.get('date_from')
                    date_to = cd.get('date_to')
                    store_obj = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
                    if type == "FLAT PER SKU":
                        if ConcessionalRate.objects.filter(store_name=store_obj, sku=sku,type=type).exists():
                            obj = ConcessionalRate.objects.filter(store_name=store_obj, sku=sku,type=type).last()
                            obj.date_to = date_from - timedelta(days=1)
                            obj.save()
                        ConcessionalRate.objects.create(store_name=store_obj,rate=rate,type=type,sku=sku,date_from=date_from,date_to=date_to)

                    elif type == "RATE PER CATEGORY":
                        ind = categories.rfind('>')
                        category = categories[ind + 2:]
                        categorydesc_obj = OcCategoryDescription.objects.filter(name=category)[0]
                        category_obj = OcCategory.objects.filter(category_id=categorydesc_obj.category_id)[0]

                        if ConcessionalRate.objects.filter(store_name=store_obj, category=category_obj,type=type).exists():
                            obj = ConcessionalRate.objects.filter(store_name=store_obj, category=category_obj,type=type).last()
                            obj.date_to = date_from - timedelta(days=1)
                            obj.save()
                        ConcessionalRate.objects.create(store_name=store_obj,type=type,rate=rate,category=category_obj,date_from=date_from,date_to=date_to)

                    else:
                        if ConcessionalRate.objects.filter(store_name=store_obj,type=type).exists():
                            obj = ConcessionalRate.objects.filter(store_name=store_obj,type=type).last()
                            obj.date_to = date_from - timedelta(days=1)
                            obj.save()
                        ConcessionalRate.objects.create(store_name=store_obj,type=type,rate=rate,date_from=date_from,date_to=date_to)

            return store_detail(request,name)
        else:
            return HttpResponse(formset.errors)
    else:
        formset = ConcessionalRateFormSet()
        return render(request, 'commission/forms.html', {'formset':formset, 'name': 'Concessional Rate'})

def promo_rate(request,name):
    if request.method == 'POST':
        formset = PromoFormSet(request.POST)
        if formset.is_valid():
            for f in formset:
                if f.has_changed():

                    cd = f.cleaned_data
                    store_name = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
                    rate = cd.get('rate')
                    sku = cd.get('sku')
                    date_from = cd.get('date_from')
                    date_to = cd.get('date_to')

                    if Promo.objects.filter(store_name=store_name,sku=sku).exists():
                        store = Promo.objects.filter(store_name=store_name,sku=sku).last()
                        store.date_to = date_from - timedelta(days=1)
                        store.save()
                    Promo.objects.create(store_name=store_name,rate=rate,sku=sku,date_from=date_from,date_to=date_to)
            return store_detail(request,name)
        else:
            return HttpResponse(formset.errors)
    else:
        print('here')
        formset = PromoFormSet()
        return render(request, 'commission/forms.html', {'formset': formset, 'name': 'Promotional Rate'})
def penalty_reason_list(request,name):
    if request.method == 'POST':
        formset = PenaltyordersFormSet(request.POST)
        if formset.is_valid():
            for f in formset:
                if f.has_changed():
                    cd = f.cleaned_data
                    store_name = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
                    reason = cd.get('reason')
                    price = cd.get('price')
                    order_id = cd.get('order_id')
                    obj = Penalty_orders.objects.filter(store_name=store_name,order_id=order_id,price=price)[0]
                    print(Penalty_orders.objects.filter(store_name=store_name,order_id=order_id).count())
                    obj.reason=reason
                    obj.save()
            return store_detail(request,name)
        else:
            return HttpResponse(formset.errors)
    else:
        formset = PenaltyordersFormSet()
        return render(request, 'commission/forms.html', {'formset':formset, 'name': 'Specify Reasons'})

def penalty_list(request,name):
    if request.method == 'POST':
        formset = PenaltyFormSet(request.POST)
        if formset.is_valid():
            for f in formset:
                if f.has_changed():
                    cd = f.cleaned_data

                    price = cd.get('price')
                    orders = cd.get('orders')
                    date_from = cd.get('date_from')
                    date_to = cd.get('date_to')
                    store_obj = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
                    if Penalty.objects.filter(store_name=store_obj).exists():
                        store = Penalty.objects.filter(store_name=store_obj).last()
                        store.date_to=date_from - timedelta(days=1)
                        store.save()
                    Penalty.objects.create(store_name=store_obj,price=price,orders=orders,date_from=date_from,date_to=date_to)
            return store_detail(request,name)
        else:
            return HttpResponse(formset.errors)
    else:
        print('here')
        formset = PenaltyFormSet()
        return render(request, 'commission/forms.html', {'formset': formset, 'name': 'Penalty Charges'})
def addcommrate(request,name):
    if request.method == 'POST':
        formset = AdditionalCommRateFormSet(request.POST)
        if formset.is_valid():
            for f in formset:

                if f.has_changed():
                    cd = f.cleaned_data

                    rate = cd.get('rate')
                    date_from = cd.get('date_from')
                    date_to = cd.get('date_to')
                    payment_gateway_pass = cd.get('payment_gateway_pass')
                    tax_inclusive = cd.get('tax_inclusive')
                    store_obj = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
                    if AdditionalCommRate.objects.filter(store_name=store_obj).exists():
                        store = AdditionalCommRate.objects.filter(store_name=store_obj).last()
                        print('exists')
                        store.date_to = date_from - timedelta(days=1)
                        store.save()
                    AdditionalCommRate.objects.create(store_name=store_obj,rate=rate,date_from=date_from,date_to=date_to,payment_gateway_pass=payment_gateway_pass,tax_inclusive=tax_inclusive)
            return store_detail(request,name)
        else:
            return HttpResponse(formset.errors)
    else:
        formset = AdditionalCommRateFormSet()
        return render(request, 'commission/forms.html', {'formset':formset, 'name': 'Additional Commission Rates'})
def reimbursement(request,name):
    if request.method == 'POST':
        formset = ReimbursementFormSet(request.POST)
        if formset.is_valid():
            for f in formset:
                if f.has_changed():
                    cd = f.cleaned_data

                    thres_amt = cd.get('thres_amt')
                    amt = cd.get('amt')
                    date_from = cd.get('date_from')
                    date_to = cd.get('date_to')
                    store_obj = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
                    if Reimbursement.objects.filter(store_name=store_obj).exists():
                        store = Reimbursement.objects.filter(store_name=store_obj).last()
                        store.date_to=date_from - timedelta(days=1)
                        store.save()
                    Reimbursement.objects.create(store_name=store_obj,thres_amt=thres_amt,amt=amt,date_from=date_from,date_to=date_to)
            return store_detail(request,name)

        else:
            return HttpResponse(formset.errors)
    else:
        print('here')
        formset = ReimbursementFormSet()
        return render(request, 'commission/forms.html', {'formset': formset, 'name': 'Reimbursements'})

def delivery_zone(request,name):
    if request.method == 'POST':
        formset = DeliveryZoneFormSet(request.POST)
        if formset.is_valid():
            for f in formset:
                if f.has_changed():

                    cd = f.cleaned_data
                    store_name = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
                    pincodes = cd.get('pincodes')
                    delivered_by = cd.get('delivered_by')
                    date_from = cd.get('date_from')
                    date_to = cd.get('date_to')

                    if DeliveryZone.objects.filter(store_name=store_name,pincodes=pincodes).exists():
                        store = DeliveryZone.objects.filter(store_name=store_name,pincodes=pincodes).last()
                        store.date_to = date_from - timedelta(days=1)
                        store.save()
                    DeliveryZone.objects.create(store_name=store_name,delivered_by=delivered_by,pincodes=pincodes,date_from=date_from,date_to=date_to)

            return store_detail(request,name)
        else:
            return HttpResponse(formset.errors)
    else:
        print('here')
        formset = DeliveryZoneFormSet()
        return render(request, 'commission/forms.html', {'formset': formset, 'name': 'Delivery Zones'})


def myFunction(request):

    if request.is_ajax():
        q = request.GET.get('term', '')
        print(q)
        stores = OcStorelocatorStore.objects.filter(store_name_backend__icontains=q)
        results = []
        for store in stores:
            drug_json = {}
            drug_json['label'] = store.store_name_backend
            drug_json['value'] = store.store_name_backend
            results.append(drug_json)
        data = json.dumps(results)
        print(results)
    else:
        print("i m here")
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def default_rate(request,name):
    if request.method == 'POST':
        c=0
        formset = DefaultRateFormSet(request.POST)
        if formset.is_valid():
            for f in formset:
                if f.has_changed():
                    c=c+1
                    cd = f.cleaned_data

                    rate = cd.get('rate')
                    date_from = cd.get('date_from')
                    date_to = cd.get('date_to')
                    payment_gateway_pass = cd.get('payment_gateway_pass')
                    tax_inclusive = cd.get('tax_inclusive')

                    store_obj = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
                    print(store_obj)
                    if DefaultRate.objects.filter(store_name=store_obj).exists():
                        store = DefaultRate.objects.filter(store_name=store_obj).last()
                        store.date_to=date_from - timedelta(days=1)
                        store.save()
                    DefaultRate.objects.create(store_name=store_obj,rate=rate,date_from=date_from,date_to=date_to,payment_gateway_pass=payment_gateway_pass,tax_inclusive=tax_inclusive)

                print(c)
            return store_detail(request,name)
        else:
            return HttpResponse(formset.errors)
    else:
        print('here')
        formset = DefaultRateFormSet()
        stores = OcStore.objects.all()
        return render(request, 'commission/forms.html', {'formset': formset, 'name': 'Base', 'stores':stores})

def gstno_change(request,name):
    if request.method == 'POST':
        gstno = request.POST['gstno']
        if GstStore.objects.filter(store_name__store_name_backend=name):
            obj = GstStore.objects.filter(store_name__store_name_backend=name)[0]
            obj.gstno = gstno
            obj.save();
        else:
            store_obj = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
            GstStore.objects.create(store_name=store_obj,gstno=gstno)
        return store_detail(request,name)


def store_detail(request,name):
    store_obj = OcStorelocatorStore.objects.filter(store_name_backend=name)[0]
    cust_id = OcCustomerpartnerToStorelocator.objects.filter(storelocator_id=store_obj.storelocator_id)[0]
    base = DefaultRate.objects.filter(store_name=store_obj).order_by('-id')[:10]
    conc = ConcessionalRate.objects.filter(store_name=store_obj).order_by('-id')[:10]
    addcomm = AdditionalCommRate.objects.filter(store_name=store_obj).order_by('-id')[:10]
    penalty = Penalty.objects.filter(store_name=store_obj).order_by('-id')[:10]
    reimbursement = Reimbursement.objects.filter(store_name=store_obj).order_by('-id')[:10]
    promo =Promo.objects.filter(store_name=store_obj).order_by('-id')[:10]
    deliveryzone = DeliveryZone.objects.filter(store_name=store_obj).order_by('-id')[:10]

    penalty_reason = Penalty_orders.objects.filter(store_name=store_obj,reason__isnull=False).order_by('-id')[:10]
    formset1 = DefaultRateFormSet(queryset=DefaultRate.objects.none())
    formset2 = ConcessionalRateFormSet(queryset=ConcessionalRate.objects.none())
    formset3 = AdditionalCommRateFormSet(queryset=AdditionalCommRate.objects.none())
    formset4 = PenaltyFormSet(queryset=Penalty.objects.none())
    formset5 = ReimbursementFormSet(queryset=Reimbursement.objects.none())
    formset6 = PromoFormSet(queryset=Promo.objects.none())
    formset7 = DeliveryZoneFormSet(queryset=DeliveryZone.objects.none())
    all_cancelled_orders = OcOrder.objects.filter(order_status_id=7,customer_id=cust_id.customer_id)
    Penalty_order = Penalty_orders.objects.all().only('order_id')
    P = []
    for penaltys in Penalty_order:
        P.append(penaltys.order_id)
    for order in all_cancelled_orders:
        if order.order_id not in P:
            Penalty_orders.objects.create(store_name=store_obj,order_id=order.order_id,price=order.total)
    gstno = None
    if GstStore.objects.filter(store_name__store_name_backend=name):
        gst_obj = GstStore.objects.filter(store_name__store_name_backend=name)[0]
        gstno = gst_obj.gstno
    formset8 = PenaltyordersFormSet(queryset=Penalty_orders.objects.filter(reason__isnull=True,store_name=store_obj))
    return render(request, 'commission/store_details.html', {'penalty_reason':penalty_reason, 'promo':promo, 'deliveryzone':deliveryzone, 'base':base, 'conc':conc, 'addcomm':addcomm, 'penalty':penalty, 'reimbursement':reimbursement,'gstno':gstno, 'formset1':formset1, 'formset2':formset2, 'formset3':formset3, 'formset4':formset4, 'formset5':formset5, 'formset6':formset6, 'formset7':formset7, 'formset8':formset8, 'name':name})
