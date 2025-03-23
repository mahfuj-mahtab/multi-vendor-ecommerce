from django.db import models

# Create your models here.
from apps.vendor.models import *
from apps.category.models import *
class Product(models.Model):
    name = models.CharField(max_length= 30)
    description = models.TextField(max_length=1000)
    banner_img = models.ImageField(upload_to='media/upload')
    price = models.FloatField()
    discount_price = models.FloatField()
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product_category')
    is_active = models.BooleanField(default=True)
    has_variation = models.BooleanField(default=False)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Variation(models.Model):
    name = models.CharField(max_length= 30)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_variant")
    banner_img = models.ImageField(upload_to='media/upload')
    price = models.FloatField()
    discount_price = models.FloatField()
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Attribute(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    variation = models.ForeignKey(Variation,on_delete=models.CASCADE,related_name="attribues")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name