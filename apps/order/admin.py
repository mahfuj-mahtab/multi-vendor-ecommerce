from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(OrderItem)
admin.site.register(Tracking_history)
