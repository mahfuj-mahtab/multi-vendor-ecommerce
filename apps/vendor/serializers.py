from rest_framework import serializers

from .models import *
from apps.user.serializers import UserSerializer
class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Vendor
        fields = '__all__'