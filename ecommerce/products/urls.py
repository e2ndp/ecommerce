from django.urls import path

from products.views import create_product, list_products, search_products

urlpatterns = [
    path('new-product/', create_product, name='create_product'),
    path('list-products/', list_products, name='list_products'),
    path('search-products/', search_products, name='search_products'),
]