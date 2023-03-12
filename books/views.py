from django.shortcuts import render
import json

jsonFile = open('books.json').read()

bookList = json.loads(jsonFile)

# Create your views here.
def index(request) :
    context = {'books': bookList}
    return render(request, 'books/index.html', context)

def show(request, id) :
    book = {}
    for b in bookList:
        if b['id'] == id :
            book = b
    context = {'book': book}
    return render(request, 'books/show.html', context)
