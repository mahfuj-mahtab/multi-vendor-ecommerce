from django.db import models
from django.contrib.auth.models import User
from apps.product.models import *
from apps.vendor.models import *

# Create your models here.
class Order(models.Model):
    status = (
        ('PENDING','PENDING'),
        ('APPROVED','APPROVED'),
        ('CANCELLED','CANCELLED'),
        ('DONE','DONE'),
        ('HOLD','HOLD'),
    )
    payment_status = (
        ('PAID','PAID'),
        ('UNPAID','UNPAID'),
        ('REFUNDED','REFUNDED'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    phone = models.CharField(max_length= 30)
    address = models.CharField(max_length= 30)
    order_price = models.FloatField()
    status = models.CharField(choices=status, default='PENDING',max_length= 30)
    payment_status = models.CharField(choices=payment_status, default='UNPAID',max_length= 30)
    tracking_info = models.CharField(max_length= 30)
    notes = models.CharField(blank=True,max_length= 30)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status


class Payment(models.Model):
    status = (
        ('PAID','PAID'),
        ('FAILED','FAILED'),
        ('REFUNDED','REFUNDED'),
  
    )
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.CharField(max_length= 30)
    status = models.CharField(choices=status, default='PENDING',max_length= 30)
    credential = models.CharField(max_length= 30)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status
class OrderItem(models.Model):

    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status
    
