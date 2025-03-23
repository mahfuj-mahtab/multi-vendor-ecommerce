from django.db import models
from django.contrib.auth.models import User
from apps.user.models import *

# Create your models here.
class Vendor(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('SUSPEND', 'SUSPEND'),
        ('WARNED', 'WARNED'),
    )
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='PENDING', max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class VendorDetails(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name='vendor_details')
    description = models.TextField(max_length=2000, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    
    # Social Media Links
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

class VendorPaymentInfo(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name='vendor_payment_info')
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    payment_account_id = models.CharField(max_length=255, blank=True, null=True)

class VendorDiscounts(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name='vendor_discounts')
    discount_percentage = models.FloatField(default=0, blank=True, null=True)
    discount_code = models.CharField(max_length=50, blank=True, null=True)
    discount_valid_until = models.DateTimeField(blank=True, null=True)

class VendorBusinessHours(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name='vendor_business_hours')
    business_hours_start = models.TimeField(blank=True, null=True)
    business_hours_end = models.TimeField(blank=True, null=True)
