from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect("book_list")
    return render(request, "bookshelf/book_form.html")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        if title and author:
            book.title = title
            book.author = author
            book.save()
            return redirect("book_list")
    return render(request, "bookshelf/book_form.html", {"book": book})
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book}
# Create your views here.
