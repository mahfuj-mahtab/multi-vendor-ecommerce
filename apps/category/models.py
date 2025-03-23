from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from apps.user.models import *


class Category(models.Model):
    status = (
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE')
    )
    name = models.CharField(max_length= 30)
    created_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description = models.TextField(max_length= 500)
    logo = models.ImageField(upload_to='media/upload')
    status = models.CharField(choices=status,default='ACTIVE',max_length= 30)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub_category')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
