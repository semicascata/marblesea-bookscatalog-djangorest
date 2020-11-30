from .models import Comment
from rest_framework import serializers
# from marblesea.apps.books.serializers import BookSerializer

class CommentSerializer(serializers.ModelSerializer):
  # book = BookSerializer(read_only=True)
  
  class Meta:
    model = Comment
    fields = ('book', 'text', 'pk')