from django.db import models
from marblesea.apps.books.models import Book
from django.contrib.auth.models import User 

class Comment(models.Model):
  book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='book')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
  text = models.TextField(blank=False)
  active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  def __int__(self):
    return self.text