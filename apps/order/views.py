from rest_framework import serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Order, Payment, OrderItem, Product, Vendor
from .serializers import *
from django.db import transaction
from django.db.models import Q
# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().select_related('user', 'vendor').prefetch_related('order_items')
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        print(serializer,'data')
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def update_status(self, request, pk=None):
        order = self.get_object()
        status = request.data.get('status')
        if status not in dict(Order.status):
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        order.status = status
        order.save()
        return Response({'message': 'Order status updated successfully'})

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().select_related('order')
    serializer_class = PaymentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
class UserOrder(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        orders = Order.objects.filter(user=user).select_related('user', 'vendor').prefetch_related('order_items')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        data = request.data
        print(request.data,'user order data')
        customer_data = request.data['customer']
        try:
            with transaction.atomic():  # Ensure atomicity
                # Extract order details
                user = request.user
                phone = customer_data.get('phone')
                address = customer_data.get('address')
                order_price = data.get('totalAmount')
                

                # Create the order
                order = Order.objects.create(
                    user=user,
                    phone=phone,
                    address=address,
                    order_price=order_price,
                )

                # Process order items
                order_items_data = data.get('order_items', [])
                for item in order_items_data:
                    product = Product.objects.get(id=item.get('id'))
                    vendor = Vendor.objects.get(id=item.get('vendor'))
                    quantity = item.get('quantity', 1)
                    unit_price = item.get('discount_price', item.get('price'))

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        vendor=vendor,
                        quantity=quantity,
                        unit_price=unit_price
                    )

               

                return Response({"message": "Order created successfully", "order_id": order.id}, status=status.HTTP_201_CREATED)

        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # serializer = OrderSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save(user=user)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)