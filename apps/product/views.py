from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import *
from .serializers import *
class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer