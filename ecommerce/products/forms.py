# from socket import fromshare
from email.mime import image
from django import forms

class  CreateProducts(forms.Form):
    name = forms.CharField(max_length=40)
    category = forms.CharField(max_length=30)
    description = forms.CharField(max_length=250)
    price = forms.FloatField()
    image = forms.ImageField(required=False)


class  CreateCombos(forms.Form):
    name = forms.CharField(max_length=40)
    category = forms.CharField(max_length=30)
    description = forms.CharField(max_length=250)
    price = forms.FloatField()