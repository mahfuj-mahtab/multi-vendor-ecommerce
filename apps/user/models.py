from django.db import models

from django.contrib.auth.models import User,AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11,null=True)
    avatar = models.ImageField(upload_to='media/upload/',null=True)
    date_of_birth = models.DateField(null=True)
