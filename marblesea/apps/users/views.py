from django.contrib.auth.models import User
from marblesea.apps.auth.serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# viewset
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def users(req):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated,])
def edit_user(req, pk):
  try:
    user = User.objects.get(pk=pk)
  except User.DoesNotExist:
    return Response({'exception': 'User not found'}, status=status.HTTP_404)

  if req.method == 'GET':
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

  if req.method == 'PUT':
    return

  if req.method == 'DELETE':
    return