from django.forms import ModelForm, Form
import django.forms as f
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'book_cover', 'description', 'price']
