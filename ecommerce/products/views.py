from multiprocessing import context
from django.shortcuts import render, redirect
from products.models import Products, Combos
from products.forms import CreateProducts, CreateCombos

#   ------------
#   | Products |
#   ------------
def create_product(request):
    if request.method == 'POST':
        form = CreateProducts(request.POST)
        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data['name'],
                category = form.cleaned_data['category'],
                description = form.cleaned_data['description'],
                price = form.cleaned_data['price']
            )
            return redirect(list_products)
            
    elif request.method == 'GET':
        form = CreateProducts()
        context = { 'form' : form }
        return render(request, 'products/new-product.html', context=context)


def list_products(request):
    products = Products.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'products/list-products.html', context=context)


def search_products(request):
    search = request.GET['search']
    products = Products.objects.filter(name__icontains=search)
    context = {
        'products' : products
    }
    return render(request, 'products/search-products.html', context=context)

#   ----------
#   | Combos |
#   ----------
def create_combos(request):
    if request.method == 'POST':
        form = CreateCombos(request.POST)
        if form.is_valid():
            Combos.objects.create(
                name = form.cleaned_data['name'],
                category = form.cleaned_data['category'],
                description = form.cleaned_data['description'],
                price = form.cleaned_data['price']
            )
            return redirect(list_combos)
            
    elif request.method == 'GET':
        form = CreateCombos()
        context = { 'form' : form }
        return render(request, 'products/new-combo.html', context=context)


def list_combos(request):
    combos = Combos.objects.all()
    context = {
        'combos' : combos
    }
    return render(request, 'products/list-combos.html', context=context)


def search_combos(request):
    search = request.GET['search']
    combos = Combos.objects.filter(name__icontains=search)
    context = {
        'combos' : combos
    }
    return render(request, 'products/search-combos.html', context=context)