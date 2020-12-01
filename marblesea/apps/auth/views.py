from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# viewset
class RegisterViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

@api_view(['POST'])
def register(req):
  serializer = RegisterSerializer(data=req.data)

  if serializer.is_valid():
    # password validation
    if req.data['password'] != req.data['password2']:
      return Response({'exception': 'Passwords dont match'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
      username=serializer.data['username'],
      email=serializer.data['email'],
      first_name=serializer.data['first_name'],
      last_name=serializer.data['last_name'],
    )
    user.set_password(req.data['password'])
    user.save()
    return Response({'details': 'User successfully registered', 'user': serializer.data}, status=status.HTTP_201_CREATED)
  else:
    return Response({'exception': 'Failed to register user'}, status=status.HTTP_400_BAD_REQUEST)
