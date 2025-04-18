from django.forms import forms

from .models import Book


class BookCreationForm(forms.Form):
    class Meta:
        model = Book