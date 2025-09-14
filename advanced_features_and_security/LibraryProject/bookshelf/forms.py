from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Only allow these fields
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 200}),
            'author': forms.Select()
        }