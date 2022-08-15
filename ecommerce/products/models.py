from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import category
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'products/', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    

class Combos(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Combo'
        verbose_name_plural = 'Combos'