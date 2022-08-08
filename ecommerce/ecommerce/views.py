from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse('Hola desde la Views')

def segundo_template(request):
    return render(request, 'template-2.html', context={})