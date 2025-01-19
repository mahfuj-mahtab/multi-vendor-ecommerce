from django.db import models

# Create your models here.
from vendor.models import *
from category.models import *
class Product(models.Model):
    name = models.CharField()
    description = models.TextField(max_length=1000)
    banner_img = models.ImageField(upload_to='/media/upload')
    price = models.FloatField()
    discount_price = models.FloatField()
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    has_variation = models.BooleanField(default=False)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name