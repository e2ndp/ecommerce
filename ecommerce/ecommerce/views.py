from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html', context={})