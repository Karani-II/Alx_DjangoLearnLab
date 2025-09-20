from rest_framework import serializers
from .models import Book 
class BookSerializer(serializers.Modelserializers):
    class meta:
        model = Book 
        fiels = ['title','author','creation_date']
