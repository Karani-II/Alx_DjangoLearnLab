from relationship_app.models import Author , Book , Library, Librarian 
Library.objects.get(name=library_name)
books_in_library = Library.books.all()
Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
Librarian.objects.get(library="")
