from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser

# viewset
class BookViewSet(viewsets.ModelViewSet):
  # api endpoint that allows member to be viewed or edited
  queryset = Book.objects.all()
  serializer_class = BookSerializer

@api_view(['GET', 'POST'])
def books(req):
  if req.method == 'GET':
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

  if req.method == 'POST':
    serializer = BookSerializer(data=req.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
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