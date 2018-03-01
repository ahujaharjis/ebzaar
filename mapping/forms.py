from django import forms
from .models import *
from django.forms import ModelForm



class ResultsForm(ModelForm):

    class Meta:
        model = Results
        fields = ['base_file','ebazr_file','vendor_file']
