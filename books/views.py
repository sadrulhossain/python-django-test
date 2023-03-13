from django.shortcuts import render
from books.models import Book


# Create your views here.
def index(request):
    bookList = Book.objects.all()
    context = {'books': bookList}
    return render(request, 'books/index.html', context)


def show(request, id):
    book = Book.objects.get(pk=id)
    context = {'book': book}
    return render(request, 'books/show.html', context)
