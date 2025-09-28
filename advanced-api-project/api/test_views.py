from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        self.client = APIClient()
        self.client.login(username="testuser", password="testpass123")

        self.author = Author.objects.create(name="John Doe")

        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2024
        )

        self.book_detail_url = reverse("book-detail", kwargs={"pk": self.book.id})

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2025
        }
        response = self.client.post(self.book_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data["title"], "New Book")

    def test_update_book(self):
        data = {"title": "Updated Title", "author": self.author.id, "publication_year": 2023}
        response = self.client.put(self.book_detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_list_books(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_permissions_required(self):
        client = APIClient()  # no login
        response = client.post(self.book_url, {
            "title": "Unauthorized Book",
            "author": self.author.id,
            "publication_year": 2025
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
