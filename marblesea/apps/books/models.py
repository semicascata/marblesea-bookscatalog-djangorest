from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=200, unique=True)
  author = models.CharField(max_length=200)
  pages = models.IntegerField(default=0, blank=True)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
  resume = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)
  def __str__(self):
    return self.title