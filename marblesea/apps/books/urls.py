from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:pk>', views.books_edit, name='book'),
    path('add/', views.add_book, name='add_books'),
]
