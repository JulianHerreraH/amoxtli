# posts/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'price', 'author', 'publisher', 'description', 'genre', 'subject', 'quality', 'image']