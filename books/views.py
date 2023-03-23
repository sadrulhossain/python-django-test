from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review
from django.views.generic import ListView, DetailView


# Create your views here.
class BookListView(ListView) :
    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(DetailView):
    model = Book
    #bookReviews = Review.objects.filter(bookId=id).order_by('-createdAt')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookReviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        return context


def booksByAuthor(request, id):
    bookList = Book.objects.filter(authors__id=id)
    context = {'book_list': bookList}
    return render(request, 'books/book_list.html', context)
def saveReview(request) :
    data = request.POST
    review = Review(book_id=data['book_id'], body=data['review_body'])
    review.save()
    return redirect('/books')