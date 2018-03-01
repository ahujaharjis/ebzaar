from django import forms
from .models import *
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.forms.models import BaseModelFormSet

class DefaultRateForm(ModelForm):
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}),required=False)
    class Meta:
        model = DefaultRate
        fields = ['rate','date_from','date_to','payment_gateway_pass','tax_inclusive']


DefaultRateFormSet = modelformset_factory(DefaultRate, form=DefaultRateForm,extra=1)

class PromoForm(ModelForm):
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = Promo
        fields = ['sku','rate','date_from','date_to']


PromoFormSet = modelformset_factory(Promo,form=PromoForm,extra=1)

class ConcessionalRateForm(ModelForm):
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    categories = forms.ChoiceField(required=False)
    def __init__(self,*args,**kwargs):
        super(ConcessionalRateForm, self).__init__(*args, **kwargs)

        list = []
        choices = OcCategory.objects.all()
        for c in choices:
            orig = OcCategoryDescription.objects.filter(category_id=c.category_id)[0]
            name=""
            while(OcCategory.objects.filter(category_id=c.parent_id).exists()):
                new = OcCategoryDescription.objects.filter(category_id=c.parent_id)[0]
                name = new.name +" > "+ name
                c = OcCategory.objects.filter(category_id=c.parent_id)[0]
            name = name + orig.name
            list.append(name)
        CHOICES = [tuple([x, x]) for x in list]
        self.fields['categories'] = forms.ChoiceField(choices=CHOICES)
        self.fields['categories'].required = False
        self.fields['categories'].widget.attrs['cols'] = 15

    class Meta:
        model = ConcessionalRate

        fields = ['type','sku','categories','rate','date_from','date_to']

    def clean(self):
        type = self.cleaned_data.get('type')

        if type == 'FLAT PER SKU':
            self.fields_required(['sku'])
        elif type == 'RATE PER CATEGORY':
            self.fields_required(['categories'])
        else:
            self.fields['sku'].disabled = True
            self.fields['categories'].disabled = True

    def fields_required(self, fields):
        """Used for conditionally marking fields as required."""
        for field in fields:
            if not self.cleaned_data.get(field, ''):
                msg = forms.ValidationError("This field is required.")
                self.add_error(field, msg)


ConcessionalRateFormSet = modelformset_factory(ConcessionalRate,form=ConcessionalRateForm,extra=1)

class PenaltyForm(ModelForm):
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    def __init__(self, *args, **kwargs):
        super(PenaltyForm, self).__init__(*args, **kwargs)
        self.fields['orders'].label = "Threshold"
    class Meta:
        model = Penalty
        fields = ['price','orders','date_from','date_to']
PenaltyFormSet = modelformset_factory(Penalty,form=PenaltyForm,extra=1)

class ReimbursementForm(ModelForm):
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = Reimbursement
        fields = ['thres_amt','amt','date_from','date_to']
ReimbursementFormSet = modelformset_factory(Reimbursement,form=ReimbursementForm,extra=1)

class DeliveryZoneForm(ModelForm):
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = DeliveryZone
        fields = ['pincodes','delivered_by','date_from','date_to']


DeliveryZoneFormSet = modelformset_factory(DeliveryZone,form=DeliveryZoneForm,extra=1)

class PenaltyordersForm(ModelForm):

    class Meta:
        model = Penalty_orders
        fields = ['order_id','reason','price']
PenaltyordersFormSet = modelformset_factory(Penalty_orders,form=PenaltyordersForm,extra=0)

class AdditionalCommRateForm(ModelForm):
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = AdditionalCommRate
        fields = ['rate','date_from','date_to','payment_gateway_pass','tax_inclusive']
AdditionalCommRateFormSet = modelformset_factory(AdditionalCommRate,form=AdditionalCommRateForm,extra=1)