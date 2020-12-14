from django.contrib.auth.models import User
from marblesea.apps.auth.serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ChangePasswordSerializer

# viewset
class UserViewSet(viewsets.ModelViewSet):
  def get_serializer_class(self):
    if self.action == ('users' or 'edit_user_admin'):
      return UserSerializer
    if self.action == 'edit_user':
      return ChangePasswordSerializer
  queryset = User.objects.all()
  # serializer_class = UserSerializer

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
  try:
    user = User.objects.get(pk=req.user.pk)
  except User.DoesNotExist:
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

  data = {
    'old_password': req.data['old_password'],
    'new_password': req.data['new_password'],
    'new_password_confirm': req.data['new_password_confirm'],
  }

  serializer = ChangePasswordSerializer(data=data)
  if serializer.is_valid():
    print('error is here, wrong serializer field')
    if req.data['new_password'] != req.data['new_password_confirm']:
      return Response({'exception': 'New passwords dont match'}, status=status.HTTP_409_CONFLICT)

    if not user.check_password(req.data['old_password']):
      print('error is here, wrong passsword')
      return Response({'exception': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)

    user.set_password(req.data['new_password'])
    user.save()
    return Response({'detail': 'Successfully changed user password for "{}"'.format(user.first_name)}, status=status.HTTP_200_OK)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)