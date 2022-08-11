from multiprocessing import context
from django.shortcuts import render, redirect
from products.models import Products
from products.forms import CreateProducts


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