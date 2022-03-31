from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Book, Order
from .forms import NewBookForm, NewAuthorForm

def index(request):
   return render(request, "shop/index.html",
   {'books':Book.objects.all()})
   

@login_required
def newBook(request):
    if request.method == "POST":
        form = NewBookForm(request.POST)

        

        if form.is_valid():
            form.instance.Poster = request.user
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "shop/newBook.html", {
           "form" : form,
           "errors" : form.errors
              })
    form = NewBookForm()
    return render(request, "shop/newBook.html", {
            "form" : form
        })

@login_required
def newAuthor(request):
   # labels = ["Имя", "Фамилия", "Отчество"] 
    if request.method == "POST": 
        form = NewAuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "shop/newAuthor.html", {
                "form": form, 
            })
    form = NewAuthorForm()
    return render(request, "shop/newAuthor.html", {
            "form" : form,
        })


def basket(request):
    goods =  Order.objects.filter(Customer=request.user)
    cost = 0
    for good in goods:
        cost += good.Book.Price
    if goods:
        mes = "message"
    else:
        mes = "no mes"
    return render(request, "shop/basket.html",
    {
        "goods":goods,
        "mes": mes,
        "cost" : cost
    })


def info(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    sth = user = book.Poster
    Authors = book.Author.all()
    info = ''
    for aut in Authors:
        info += f' {aut}, '

    info = info[:-2]

    try:
        Order.objects.get(Book=book)
        inList = True
    except Order.DoesNotExist:
        inList = False


    return render(request, "shop/info.html", {
            "book":book, 
            "inList" : inList,
            "info" : info,
          "sth"  : sth
    }
    )

def delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return HttpResponseRedirect(reverse("index"))


def edit(request, book_id):
    labels = ["Название", "Описание", "Цена", "Картинка", "Автор"]
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        form = NewBookForm(request.POST)
        

        if form.is_valid():
            book.Title = form.cleaned_data["Title"]
            book.Description = form.cleaned_data["Description"]
            book.Price = form.cleaned_data["Price"]
            book.Photo = form.cleaned_data["Photo"]
            book.Author.set(form.cleaned_data["Author"])
            book.save()

            
            
            return HttpResponseRedirect(reverse("index"))
    
    
    initial_ = {
    "Title": book.Title,
    "Description" : book.Description,
    "Price" : book.Price,
    "Photo" : book.Photo,
    
    }
    
    form = NewBookForm(request.POST or None, initial=initial_)
    
    return render(request, "shop/edit.html",
    {
        "form" : zip(form, labels),
        "book" : book
        
    })

def shoplistChange(request, book_id):
    _book = Book.objects.get(pk=book_id)
    user = request.user
    order = Order(Customer = user, Book=_book)
    order.save()

    try:
        Order.objects.get(Book=_book)
        inList = True
    except Order.DoesNotExist:
        inList = False

    return render(request, "shop/info.html", {
            "book" : _book,
            "inList" : inList 
        })
     
def shoplistRemove(request, book_id):
     user = request.user
     book = Book.objects.get(pk=book_id)

     Order.objects.filter(Customer=user, Book=book).delete()
     return HttpResponseRedirect(reverse("basket"))

          