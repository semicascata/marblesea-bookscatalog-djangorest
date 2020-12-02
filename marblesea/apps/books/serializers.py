from .models import Book
from rest_framework import serializers
# from django.contrib.auth.models import User 
# from marblesea.apps.auth.serializers import UserSerializer

class BookSerializer(serializers.ModelSerializer):
  # publisher_user = UserSerializer(User)

  class Meta:
    model = Book
    fields = ('pk', 'title', 'author', 'pages', 'publisher_user')
    # fields = '__all__'