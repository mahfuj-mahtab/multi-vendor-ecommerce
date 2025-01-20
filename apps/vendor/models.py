from django.db import models
from django.contrib.auth.models import User
from apps.user.models import *

# Create your models here.
class Vendor(models.Model):
    status = (
        ('PENDING' , 'PENDING'),
        ('APPROVED' , 'APPROVED'),
       ( 'SUSPEND' , 'SUSPEND'),
       ( 'WARNED', 'WARNED'),
    )
    name = models.CharField(max_length= 30)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to="media/upload")
    status = models.CharField(choices=status, default='PENDING',max_length= 30)
    rating = models.FloatField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name