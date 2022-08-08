from unicodedata import category
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    
