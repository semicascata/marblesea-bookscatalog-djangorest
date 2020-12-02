from .models import Comment
from rest_framework import serializers
from django.contrib.auth.models import User 
from marblesea.apps.auth.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
  user = UserSerializer(User)

  class Meta:
    model = Comment
    fields = ('book', 'user', 'text', 'pk')