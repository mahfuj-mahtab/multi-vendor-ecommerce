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
from apps.order.models import *
from apps.order.serializers import *
class VendorAllProductShow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        products = Product.objects.filter(vendor = vendor).order_by('-createdAt')
        return Response({"data" : ProductSerializer(products,many = True).data},status = status.HTTP_200_OK)
    def post(self,request):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        serializers = ProductSerializer(data = request.data)
        if(serializers.is_valid()):
            serializers.save(vendor = vendor)
            return Response({"msg" : 'Product successfully created'},status = status.HTTP_201_CREATED)
        else:
            return Response({"error" : serializers.errors},status = status.HTTP_400_BAD_REQUEST)
class VendorSingleProductShow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,p_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        product = get_object_or_404(Product,id = p_id,vendor = vendor)
        return Response({"data" : ProductSerializer(product).data},status = status.HTTP_200_OK)

    def patch(self,request,p_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        product = get_object_or_404(Product,id = p_id,vendor = vendor)
        serializers = ProductSerializer(product,data = request.data,partial = True)
        if(serializers.is_valid()):
            serializers.save(vendor = vendor)
            return Response({"msg" : 'Product successfully '},status = status.HTTP_200_OK)
        else:
            return Response({"error" : serializers.errors},status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request,p_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        product = get_object_or_404(Product,id = p_id,vendor = vendor)
        product.delete()
        return Response({"msg" : 'Product delete success'},status = status.HTTP_200_OK)


class VendorAllProductsOrderShow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        orders = Order.objects.filter(vendor = vendor).order_by('-createdAt')
        return Response({"data" : OrderSerializer(orders,many = True).data},status = status.HTTP_200_OK)
class VendorAllProductsSingleOrderShow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,o_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        order = get_object_or_404(Order,id = o_id,vendor = vendor)
        return Response({"data" : OrderSerializer(order).data},status = status.HTTP_200_OK)
    def patch(self,request,o_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        order = get_object_or_404(Order,id = o_id,vendor = vendor)
        serializers = OrderSerializer(order,data = request.data,partial = True)
        if(serializers.is_valid()):
            serializers.save(vendor = vendor)
            return Response({"msg" : 'Order successfully updated'},status = status.HTTP_200_OK)
        return Response({"error" : serializers.errors},status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request,o_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        order = get_object_or_404(Order,id = o_id,vendor = vendor)
        order.delete()

        return Response({"msg" : 'Order delete success'},status = status.HTTP_200_OK)
class VendorSingleOrderItemShow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,o_id,ot_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        order = get_object_or_404(Order,id = o_id,vendor = vendor)
        order_item = get_object_or_404(OrderItem,id = ot_id,vendor = vendor,order = order)
        return Response({"data" : OrderItemSerializer(order_item).data},status = status.HTTP_200_OK)
    def patch(self,request,o_id,ot_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        order = get_object_or_404(Order,id = o_id,vendor = vendor)
        order_item = get_object_or_404(OrderItem,id = ot_id,vendor = vendor,order = order)
        product = get_object_or_404(Product,id = request.data['product'])
        serializers = OrderItemSerializer(order_item,data = request.data,partial = True)

        if(serializers.is_valid()):
            serializers.save(vendor = vendor,order = order,product = product)
            return Response({"msg" : 'Order item successfully updated'},status = status.HTTP_200_OK)
        return Response({"error" : serializers.errors},status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request,o_id,ot_id):
        user = request.user
        vendor = get_object_or_404(Vendor,user = user)
        order = get_object_or_404(Order,id = o_id,vendor = vendor)
        order_item = get_object_or_404(OrderItem,id = ot_id,vendor = vendor,order = order)
        order_item.delete()

        return Response({"msg" : 'Order item delete success'},status = status.HTTP_200_OK)


        