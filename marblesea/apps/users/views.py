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

@api_view(['GET', 'DELETE'])
@permission_classes([IsAdminUser,])
def edit_user_admin(req, pk):
  try:
    user = User.objects.get(pk=pk)
  except User.DoesNotExist:
    return Response({'exception': 'User not found'}, status=status.HTTP_404)

  if req.method == 'GET':
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

  if req.method == 'DELETE':
    user.delete()
    return Response({'message': 'User {} successfully deleted'.format(user.username)}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated,])
def edit_user(req):
  return