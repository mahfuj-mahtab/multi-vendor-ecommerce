from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
class CategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
