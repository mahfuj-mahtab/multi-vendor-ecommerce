from rest_framework import serializers
from .models import *

class TrackingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking_history
        fields = ['id', 'order', 'tracking_status', 'tracking_notes', 'createdAt', 'updatedAt'] 


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'unit_price', 'createdAt', 'updatedAt']

class OrderSerializer(serializers.ModelSerializer):
    # order_items = OrderItemSerializer(many=True, required=False, read_only=True)
    # tracking_history = TrackingHistorySerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'payment_method', 'status', 'credential', 'createdAt', 'updatedAt']
        read_only_fields = ['status', 'createdAt', 'updatedAt']

