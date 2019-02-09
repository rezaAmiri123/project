from django import forms
from .models import Book, Publisher, Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email',]


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'city', 'country',
                  'address', 'website', 'description']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher',
                  'num_page', 'publication_date',]
