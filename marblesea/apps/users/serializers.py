from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.ModelSerializer):
  old_password = serializers.CharField(required=True)
  new_password = serializers.CharField(required=True)
  new_password_confirm = serializers.CharField(required=True)
  
  class Meta:
    model = User
    fields = ('old_password', 'new_password', 'new_password_confirm')

