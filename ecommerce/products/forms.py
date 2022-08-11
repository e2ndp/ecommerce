# from socket import fromshare
from django import forms

class  CreateProducts(forms.Form):
    name = forms.CharField(max_length=40)
    category = forms.CharField(max_length=30)
    description = forms.CharField(max_length=250)
    price = forms.FloatField()


class  CreateCombos(forms.Form):
    name = forms.CharField(max_length=40)
    category = forms.CharField(max_length=30)
    description = forms.CharField(max_length=250)
    price = forms.FloatField()