from django.urls import path

from products.views import create_product, delete_combo, list_products, delete_product, update_product, search_products, buy_product\
    , create_combo, list_combos, delete_combo, update_combo, search_combos, buy_combos

urlpatterns = [
    path('new-product/', create_product, name='create_product'),
    path('list-products/', list_products, name='list_products'),
    path('update-product/<int:pk>/', update_product, name='update_product'),
    path('delete-product/<int:pk>/', delete_product, name="delete-product"),
    path('search-products/', search_products, name='search_products'),
    path('buy-product/<int:pk>/', buy_product, name='buy_product'),
    
    path('new-combo/', create_combo, name='create_combo'),
    path('list-combos/', list_combos, name='list_combos'),
    path('update-combo/<int:pk>/', update_combo, name='update_combo'),
    path('delete-combo/<int:pk>/', delete_combo, name='delete_combo'),
    path('search-combos/', search_combos, name='search_combos'),
    path('buy-combo/<int:pk>/', buy_combos, name='buy_combos'),
]