from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# viewset
class BookViewSet(viewsets.ModelViewSet):
  # api endpoint that allows member to be viewed or edited
  queryset = Book.objects.all()
  serializer_class = BookSerializer

@api_view(['GET',])
# @permission_classes([IsAuthenticated,])
def books(req):
  books = Book.objects.order_by('-author').filter(active=True)
  serializer = BookSerializer(books, many=True)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def add_book(req):
  data = {
    'title': req.data['title'],
    'author': req.data['author'],
    'pages': req.data['pages'],
    'photo': req.data['photo'],
    'resume': req.data['resume'],
    'publisher_user': req.user.pk,
  }

  serializer = BookSerializer(data=data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def books_edit(req, pk):
  try:
    book = Book.objects.get(pk=pk)
  except Book.DoesNotExist:
    return Response({'exception': 'Book not found by Id {}'.format(pk)}, status=status.HTTP_404_NOT_FOUND)

  if req.method == 'GET':
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)

  if req.method == 'PUT':
    serializer = BookSerializer(book, data=req.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if req.method == 'DELETE':
    book.delete()
    return Response({'message': 'Book "{}" was successfully deleted'.format(book.title)})