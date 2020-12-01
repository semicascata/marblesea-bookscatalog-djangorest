from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
  username = serializers.CharField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    max_length=60,
    min_length=6,
    write_only=True, 
    required=True, 
    validators=[validate_password]
  )
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = User
    fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }

    # validate if passwords match
    # def validate(self, attrs):
    #   if attrs['password'] != attrs['password2']:
    #     raise serializers.ValidationError({
    #       'InvalidCredentials': 'Passwords dont match'
    #     })
    #     return attrs

    # def create(self, validated_data):
    #   user = User.objects.create(
    #     username=validated_data['username'],
    #     email=validated_data['email'],
    #     first_name=validated_data['first_name'],
    #     last_name=validated_data['last_name'],
    #   )

    #   user.set_password(validated_data['password'])
    #   user.save()
    #   return user