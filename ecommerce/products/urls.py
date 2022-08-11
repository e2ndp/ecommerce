from django.urls import path

from products.views import create_product, list_products, search_products, create_combos, list_combos, search_combos

urlpatterns = [
    path('new-product/', create_product, name='create_product'),
    path('list-products/', list_products, name='list_products'),
    path('search-products/', search_products, name='search_products'),
    path('new-combo/', create_combos, name='create_combo'),
    path('list-combos/', list_combos, name='list_combos'),
    path('search-combos/', search_combos, name='search_combos'),
]