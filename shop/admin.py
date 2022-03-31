from django.contrib import admin
from .models import Book, Author, Order

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Order)
