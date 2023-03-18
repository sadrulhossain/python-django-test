from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookListView.as_view(), name="book.list"),
    path('book/<int:pk>', views.BookDetailView.as_view(), name="book.show"),
    path('book/saveReview', views.saveReview, name="book.saveReview"),

]
