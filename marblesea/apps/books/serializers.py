from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ('title', 'author', 'pages', 'resume', 'created_at',)
    # fields = '__all__'