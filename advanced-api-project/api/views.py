from rest_framework import generics , filters 
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book 
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title','author', 'publication_year']
    search_fields = ['title','author__name']
    ordering_fields = ['title','publication_year']
    ordering = ['title']

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]
# Create your views here.
