from django.contrib import admin
from django.urls import path, include

from ecommerce.views import saludo, segundo_template
from products.views import create_product, list_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'),
    path('template-2/', segundo_template, name='segundo_template'),
    path('products/', include('products.urls')),
]
