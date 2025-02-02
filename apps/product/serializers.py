from rest_framework import serializers
from .models import *
class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    product_variant = VariantSerializer(many = True,read_only = True)
    class Meta:
        model = Product
        fields = '__all__'