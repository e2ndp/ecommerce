from itertools import product
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


def delete_product(request, pk):
    if request.method == 'GET':
        product = Products.objects.get(id=pk)
        context = {
            'product' : product
        }
        return render(request, 'products/delete-product.html', context=context)
    
    elif request.method == 'POST':
        product = Products.objects.get(id=pk)
        product.delete()
        return redirect(list_products)
    

def update_product(request, pk):
    if request.method == 'POST':
        form = CreateProducts(request.POST)
        if form.is_valid():
            product = Products.objects.get(id=pk)
            product.name = form.cleaned_data['name']
            product.category = form.cleaned_data['category']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.save()
            
            return redirect(list_products)
            
    
    elif request.method == 'GET':
        product = Products.objects.get(id=pk)
        form = CreateProducts(initial={'name':product.name,
                                       'category':product.category,
                                       'description':product.description,
                                       'price':product.price
                                       })
        context = {
            'form' : form
        }
        return render(request, 'products/update-product.html', context=context)


#   ----------
#   | Combos |
#   ----------
def create_combo(request):
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


def update_combo(request, pk):
    if request.method == 'POST':
        form = CreateCombos(request.POST)
        if form.is_valid():
            combo = Combos.objects.get(id=pk)
            combo.name = form.cleaned_data['name']
            combo.category = form.cleaned_data['category']
            combo.description = form.cleaned_data['description']
            combo.price = form.cleaned_data['price']
            combo.save()
            
            return redirect(list_combos)
    
    elif request.method == 'GET':
        combo = Combos.objects.get(id=pk)
        form = CreateCombos(initial={'name':combo.name,
                                     'category':combo.category,
                                     'description':combo.description,
                                     'price':combo.price
                                     })
        context = {
            'form' : form
        }
        return render(request, 'products/update-combo.html', context=context)


def delete_combo(request, pk):
    if request.method == 'GET':
        combo = Combos.objects.get(id=pk)
        context = {
            'combo' : combo
        }
        return render(request, 'products/delete-combo.html', context=context)
    
    elif request.method == 'POST':
        combo = Combos.objects.get(id=pk)
        combo.delete()
        return redirect(list_combos)