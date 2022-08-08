from multiprocessing import context
from django.shortcuts import render
from products.models import Products


def create_product(request):
    new_product = Products.objects.create(
        name = 'Alfajores Chocolate 12u',
        category = 'Alfajores',
        description = 'Alfajores "Havana" -Chocolate- 12u',
        price = 10,
    )
    context = {
        'new_product' : new_product
    }
    return render(request, 'new-product.html', context=context)

def list_products(request):
    products = Products.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'list-products.html', context=context)