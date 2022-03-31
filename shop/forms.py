
from django import forms
from django.forms import widgets

from .models import Book, Author

class NewAuthorForm(forms.ModelForm):
    pass

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =  ['Title', 'Description', 'Price', 'Photo', 'Author']
        widgets = {
            'Description':widgets.Textarea(attrs={'cols' : 60, 'rows' : 10, 'class' : 'form-control'}),
            'Author': widgets.SelectMultiple()
        }

class NewAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['FirstName', 'LastName', 'Patronymic']