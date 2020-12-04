from .models import List
from .serializers import ListSerializer, ListRetrieveSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from marblesea.apps.books.models import Book
from marblesea.apps.books.serializers import BookSerializer
import json

# viewset
class ListViewSet(viewsets.ModelViewSet):
  def get_serializer_class(self):
    if self.action == 'my_books':
      return ListSerializer
    if self.action == 'add_list':
      return ListRetrieveSerializer
  # queryset = List.objects.all()
  # serializer_class = ListSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def my_books(req):
  try:
    # user list
    user = req.user.pk
    books_list = List.objects.filter(user_id=user)
    serializer = ListSerializer(books_list, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
  except List.DoesNotExist:
    return Response({
      'exception': 'There is no book on the user list'
      }, 
      status=status.HTTP_404_NOT_FOUND
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def add_list(req, pk):
  # request user
  user = req.user.pk

  # data
  data = {
    'book': pk,
    'user': user
  }

  serializer = ListRetrieveSerializer(data=data)
  if serializer.is_valid():
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated,])
def edit_list(req, pk):
  if req.method == 'PUT':
    # book_list by id
    book_list = List.objects.get(book_id=pk)

    # data changed
    # data = { 'read': 'READ' }
    serializer = ListSerializer(book_list, data=req.data, partial=True)

    if serializer.is_valid():
      serializer.save()
      return Response({'detail': 'Listing book changed, Id: {}'.format(pk)}, status=status.HTTP_200_OK)
    else:
      return Response({'exception': 'Failed to update book list by Id {}'.format(pk)}, status=status.HTTP_400_BAD_REQUEST)

  if req.method == 'DELETE':
    return