from relationship_app import Author , Book, Library, Librarian 
books_by_author = Book.objects.filter(author=author)
librarian = Librarian.objects.get(library=library)

