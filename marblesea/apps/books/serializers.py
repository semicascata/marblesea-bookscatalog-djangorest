from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ('pk', 'title', 'author', 'pages',)
    # fields = '__all__'