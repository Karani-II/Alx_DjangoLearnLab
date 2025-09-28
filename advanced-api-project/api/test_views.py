from rest_framework.test import APIRequestFactory 
from django.test import TestCase 
from .models import Book 
class BookTestCase(TestCase):
    def setUp(Self):
        Book.objects.create()