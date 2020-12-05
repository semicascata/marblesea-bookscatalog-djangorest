from .models import List
from rest_framework import serializers
from marblesea.apps.books.serializers import BookSerializer
from marblesea.apps.books.models import Book

class ListSerializer(serializers.ModelSerializer):
  # STATUS = {
  #   'READ': 'Read',
  #   'NOT_READ': 'Not_Read',
  # }
  
  # read = serializers.ChoiceField(choices=STATUS, allow_null=True)
  book = BookSerializer(Book, read_only=True)
  class Meta:
    model = List
    fields = ('pk', 'user', 'book', 'read')

class AddListSerializer(serializers.ModelSerializer):
  class Meta:
    model = List
    fields = ('user', 'book',)