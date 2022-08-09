from django.contrib import admin
from products.models import Products

# admin.site.register(Products)

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_active']
