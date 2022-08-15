from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from ecommerce.views import index, nosotros
#from products.views import create_product, list_products, create_combos, list_combos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('nosotros/', nosotros, name='nosotros'),
    
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
