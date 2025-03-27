from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, PaymentViewSet,UserOrder ,StripeCheckout
from django.urls import path
# router = DefaultRouter()
# router.register('orders', UserOrder,name = 'user_order')
# router.register('payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path ('orders/', UserOrder.as_view(), name='UserOrder'),
    path ('create-checkout-session/', StripeCheckout.as_view(), name='checkout'),
]