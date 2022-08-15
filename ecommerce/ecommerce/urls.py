from django.contrib import admin
from django.urls import path, include

from ecommerce.views import index, nosotros
#from products.views import create_product, list_products, create_combos, list_combos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('nosotros/', nosotros, name='nosotros'),
    
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
]
