from django.urls import path
from . import views

urlpatterns = [
    path('bookslist/', views.my_books, name='my_books'),
    path('addlist/<int:pk>', views.add_list, name='add_list'),
    path('editlist/<int:pk>', views.edit_list, name='edit_list'),
]
