from rest_framework import serializers
from .models import *
from apps.order.serializers import OrderSerializer
class UserSerializer(serializers.ModelSerializer):
    user_orders = OrderSerializer(many = True,read_only = True)
    class Meta:
        model = CustomUser
        exclude = ("password",)
class CustomUserSerializer(serializers.ModelSerializer):
    user_orders = OrderSerializer(many = True,read_only = True)
    class Meta:
        model = CustomUser
        fields = '__all__'
    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Ensure password exists
        user = CustomUser(**validated_data)  # Create user instance without saving
        
        if password:
            user.set_password(password)  # Hash password properly
        
        user.save()  # Save user with hashed password
        return user
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  # Extract password safely

        for attr, value in validated_data.items():
            setattr(instance, attr, value)  # Update other fields normally

        if password:
            instance.set_password(password)  # Hash new password

        instance.save()
        return instance