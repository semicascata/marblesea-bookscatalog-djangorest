from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('books/<int:pk>', views.books_edit, name='book'),
    path('books/add', views.add_book, name='add_books'),
]
