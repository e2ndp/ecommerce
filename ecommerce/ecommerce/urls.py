from django.contrib import admin
from django.urls import path, include

from ecommerce.views import homepage, nosotros
from products.views import create_product, list_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name='home'),
    path('nosotros/', nosotros, name='nosotros'),
    path('products/', include('products.urls')),
]
