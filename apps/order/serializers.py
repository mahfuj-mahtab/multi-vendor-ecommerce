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
    order_items = OrderItemSerializer(many=True, required=False)
    tracking_history = TrackingHistorySerializer(many=True, required=False)
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'vendor', 'phone', 'address', 'order_price', 'status', 
            'payment_status', 'tracking_info', 'notes', 'createdAt', 'updatedAt', 'order_items'
        ]
        read_only_fields = ['status', 'payment_status', 'createdAt', 'updatedAt']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items', [])
        order = Order.objects.create(**validated_data)
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'payment_method', 'status', 'credential', 'createdAt', 'updatedAt']
        read_only_fields = ['status', 'createdAt', 'updatedAt']

