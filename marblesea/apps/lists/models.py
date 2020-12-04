from django.db import models
from django.contrib.auth.models import User
from marblesea.apps.books.models import Book

class List(models.Model):
  class Status(models.TextChoices):
    READ = 'Read'
    NOT_READ = 'Not_Read'

  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_books')
  book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='book_list', unique=True)
  read = models.CharField(max_length=8, choices=Status.choices, blank=True, default=Status.NOT_READ)
  def __int__(self):
    return self.read
