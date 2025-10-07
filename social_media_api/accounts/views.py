from django.shortcuts import render 
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny 
from rest_framework.authtoken.models import Token 
from django.contrib.auth import authenticate 
from .models import CustomUser 
from .serializers import RegisterSerializer, CustomUserSerializers

class RegisterView(generics.CreateAPIView): 
    queryset = CustomUser.objects.all() 
    serializer_class = RegisterSerializer 
    permission_classes = [AllowAny]

def create(self, request, *args, **kwargs): 
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True) 
    user = serializer.save() 
    token, _ = Token.objects.get_or_create(user=user) 
    return Response({ 
        "user": CustomUserSerializers(user).data, 
        "token": token.key 
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView): 
    permission_classes = [AllowAny] 
    def post(self, request, *args, **kwargs): 
        username = request.data.get('username') 
        password = request.data.get('password') 
        user = authenticate(username=username, password=password) 
        if user: 
           token, _ = Token.objects.get_or_create(user=user) 
        return Response({ 
            "token": token.key, 
            "user": CustomUserSerializers(user).data 
        }) 
    return Response({"error": "Invalid credentials"}, 
status=status.HTTP_400_BAD_REQUEST)