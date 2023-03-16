from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review


# Create your views here.
def index(request):
    bookList = Book.objects.all()
    context = {'books': bookList}
    return render(request, 'books/index.html', context)


def show(request, id):
    book = get_object_or_404(Book, pk=id)
    bookReviews = Review.objects.filter(bookId=id).order_by('-createdAt')
    context = {'book': book, 'bookReviews': bookReviews}
    return render(request, 'books/show.html', context)

def saveReview(request) :
    data = request.POST
    review = Review(bookId=data['book_id'], body=data['review_body'])
    review.save()
    return redirect('/books')