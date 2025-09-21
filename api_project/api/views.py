from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated , IsAdminUser 
from rest_framework.authentication import TokenAuthentication 
from .serializers import BookSerializer 
class BookList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
# Create your views here.
