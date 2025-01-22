from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from apps.product.models import *
from apps.product.serializers import *
from .serializers import *
class VendorAllProductShow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        products = Product.objects.filter(vendor = vendor)
        return Response({"data" : ProductSerializer(products,many = True).data},status = status.http_200_ok)
    def post(self,request):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        serializers = ProductSerializer(data = request.data)
        if(serializers.is_valid()):
            serializers.save(vendor = vendor)
            return Response({"msg" : 'Product successfully created'},status = status.http_201_created)
        else:
            return Response({"error" : serializers.errors},status = status.http_400_bad_request)
class VendorSingleProductShow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,p_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        product = get_object_or_404(Product,id = p_id,vendor = vendor).order_by('-createdAt')
        return Response({"data" : ProductSerializer(product).data},status = status.http_200_ok)

    def patch(self,request,p_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        product = get_object_or_404(Product,id = p_id,vendor = vendor)
        serializers = Product(product,data = request.data,partial = True)
        if(serializers.is_valid()):
            product.save(vendor = vendor)
            return Response({"msg" : 'Product successfully '},status = status.http_200_ok)
        else:
            return Response({"error" : serializers.errors},status = status.http_400_bad_request)
    def delete(self,request,p_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        product = get_object_or_404(Product,id = p_id,vendor = vendor)
        product.delete()
        return Response({"msg" : 'Product delete success'},status = status.http_200_ok)


        