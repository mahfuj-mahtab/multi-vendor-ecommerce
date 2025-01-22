from rest_framework import serializers
from .models import *

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many = True)
    order_payment = PaymentSerializer(many = True)
    class Meta:
        model = Order
        fields = '__all__'

