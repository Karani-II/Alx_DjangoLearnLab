from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
from .models import Library 
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
def register(request):
    return render(request, "relationship_app/register.html")
def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'profile') and user.profile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'profile') and user.profile.role == 'Member'
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

