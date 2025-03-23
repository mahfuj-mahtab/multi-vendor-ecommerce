from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Vendor)
admin.site.register(VendorDetails)
admin.site.register(VendorPaymentInfo)
admin.site.register(VendorDiscounts)
admin.site.register(VendorBusinessHours)    