from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, PaymentViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='order')
router.register('payments', PaymentViewSet, basename='payment')

urlpatterns = router.urls