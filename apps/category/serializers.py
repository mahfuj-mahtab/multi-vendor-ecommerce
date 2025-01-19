from rest_framework import serializers
from .models import *
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer(many = True)
    class Meta:
        model = Category
        fields = '__all__'