from django.views.generic import DetailView
from django.shortcuts import render
from .models import Book 
def all_books(request):
books = Book.objects.all() 
context = {'book_list': books}
return render (request, 'book/book_list', context)

# Create your views here.
