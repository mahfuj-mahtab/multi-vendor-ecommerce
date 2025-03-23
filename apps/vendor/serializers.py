from rest_framework import serializers

from .models import *
from apps.user.serializers import UserSerializer
class VendorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorDetails
        fields = '__all__'
class VendorPaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPaymentInfo
        fields = '__all__'
class VendorDiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorDiscounts
        fields = '__all__'
class VendorBusinessHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorBusinessHours
        fields = '__all__'  
class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    vendor_details = VendorDetailsSerializer(many=True,read_only=True)
    vendor_payment_info = VendorPaymentInfoSerializer(many=True,read_only=True)
    vendor_discounts = VendorDiscountsSerializer(many=True,read_only=True)
    vendor_business_hours = VendorBusinessHoursSerializer(many=True,read_only=True)
    class Meta:
        model = Vendor
        fields = '__all__'

