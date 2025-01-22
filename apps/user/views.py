from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate,login
from .serializers import UserSerializer  # Ensure you have a UserSerializer defined

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
            data = {
                'refresh' : str(refresh),
                'access' : str(refresh.access_token),
                'data' : UserSerializer(user).data
            }
            return Response({"message": data}, status=status.HTTP_200_OK)
        else:
            # Handle failed login
            return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)
