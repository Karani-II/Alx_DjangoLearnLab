from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework.views import APIView
from .serializers import CustomUserSerializers 
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
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

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CustomUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers


class FollowUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, pk=user_id)

        if target_user == request.user:
            return Response({'error': 'You cannot follow yourself.'},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target_user)
        return Response({'message': f'You are now following {target_user.username}.'},
                        status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, pk=user_id)

        if target_user == request.user:
            return Response({'error': 'You cannot unfollow yourself.'},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target_user)
        return Response({'message': f'You have unfollowed {target_user.username}.'},
                        status=status.HTTP_200_OK)
