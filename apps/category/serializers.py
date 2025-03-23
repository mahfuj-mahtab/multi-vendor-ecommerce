from rest_framework import serializers
from .models import *

from apps.product.serializers import *
class CategorySerializer(serializers.ModelSerializer):
    sub_category = serializers.SerializerMethodField()
    product_category = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
    def get_sub_category(self, obj):
        sub_category = obj.sub_category.all()
        serializer = CategorySerializer(sub_category, many=True)
        return serializer.data