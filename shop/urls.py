from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views



urlpatterns = [
    path("",views.index, name="index"),
    path("newBook", views.newBook, name="newBook"),
    path("newAuthor", views.newAuthor, name="newAuthor"),
    path("basket", views.basket, name="basket"),
    path("info/<int:book_id>", views.info, name="info"),
    path("delete/<int:book_id>", views.delete, name="delete"),
    path("edit/<int:book_id>", views.edit, name="edit"),
    path("shoplistChange/<int:book_id>", views.shoplistChange, name="shoplistChange"),
    path("shoplistRemove/<int:book_id>", views.shoplistRemove, name="shoplistRemove")
]