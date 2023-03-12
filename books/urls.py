from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('book/<int:id>', views.show, name="book.show"),
]
