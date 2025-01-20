"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from apps.category.views import *
from apps.product.views import *

category_router = DefaultRouter()
category_router.register(r'', CategoryView, basename='category')
product_router = DefaultRouter()
product_router.register(r'', ProductView, basename='product')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("apps.user.urls")),
    path("api/v1/category/", include(category_router.urls)),
    path("api/v1/products/", include(product_router.urls)),
]
