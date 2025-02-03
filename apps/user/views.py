from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate,login,logout
from .serializers import UserSerializer, CustomUserSerializer  # Ensure you have a UserSerializer defined
from apps.vendor.models import *
from apps.order.models import *
from apps.order.serializers import *
class UserRegister(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Registration Done"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class UserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and Password cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

        # Assuming email is used as the username for authentication
        user = authenticate(request, username=email.split("@")[0], password=password)

        if user is not None:
            if user.is_staff or user.is_superuser:
                return Response({"error": "Invalid email or password."}, status=status.HTTP_403_FORBIDDEN)
            refresh = RefreshToken.for_user(user)
            is_vendor = False
            vendor_details = ''
            try:
                vendor = Vendor.objects.get(user=user)
                is_vendor = True 
                # TODO : RETURN VENDOR SERIALIZER INFO  
                # vendor_details = 
            except Vendor.DoesNotExist:
                pass  

            data = {
                'refresh' : str(refresh),
                'access' : str(refresh.access_token),
                'data' : UserSerializer(user).data,
                'email_verified' : user.email_verified,
                'phone_verified' : user.phone_verified,
                'is_vendor' : is_vendor,
                               
            }
            return Response({"message": data}, status=status.HTTP_200_OK)
        else:
            # Handle failed login
            return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogOut(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        logout(request)
        return Response({"message" : "Logout"},status = 200)
    
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = UserSerializer(request.user).data
        return Response({"data": user},status = 200)
class UserProfileEdit(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializers = CustomUserSerializer(request.user, data = request.data, partial = True)
        if(serializers.is_valid()):
            serializers.save()
            return Response({"message": "User info updated"},status = 200)
        else:
            return Response({"error":serializers.errors}, status = 403)
class UserOrder(APIView):
    def post(self,request):
        user = None
        if(request.user.is_authenticated):
            user = request.user
        serializers = OrderSerializer(data = request.data)
        if(serializers.is_valid()):
            serializers.save(user = user)
            return Response({"message": "Order Created"}, status = 201)
        else:
            return Response({"error": serializers.errors}, status = 403)
        
class UserSingleOrder(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,o_id):
        user = request.user
        order = get_object_or_404(Order,id = o_id, user = user)
        return Response({"data" : OrderSerializer(order).data},status = 200)
