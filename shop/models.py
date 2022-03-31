from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


class User(AbstractUser):
    pass

class Author(models.Model):
    FirstName = models.CharField(max_length=64, blank=True, default='')
    LastName = models.CharField(max_length=64, blank=True, default='')
    Patronymic = models.CharField(max_length=64, blank=True, default='')


    def __str__(self):
        return f'{self.LastName} {self.FirstName} {self.Patronymic}'
    

class Book(models.Model):
    Title = models.CharField(max_length=64)
    Description = models.CharField(max_length=400)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Photo = models.URLField(max_length=10000, blank=True, null=True)
    Author = models.ManyToManyField(Author, blank=True, default='', related_name='books')
    Poster = models.ForeignKey(User, on_delete=CASCADE, related_name='postedBooks', default='')
   
   

    def __str__(self):
        return f'{self.Author}: {self.Title}'


class Order(models.Model):
    Customer = models.ForeignKey(User, on_delete=CASCADE, related_name="purchase")
    Book = models.ForeignKey(Book, on_delete=CASCADE)
    Count = models.IntegerField(default=1)