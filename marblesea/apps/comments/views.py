from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from marblesea.apps.books.models import Book

# viewset
class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

# comments relation with books
@api_view(['GET', 'POST'])
def comments(req, pk):
  try:
    book = Book.objects.get(pk=pk) # get the book from id
    comments = Comment.objects.order_by('-created_at').filter(book=pk) # get all the comments for the single book
  except Book.DoesNotExist:
    return Response({'exception': 'Comments not found for the book by Id {}'.format(pk)}, status=status.HTTP_404_NOT_FOUND)

  # requests
  if req.method == 'GET':
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  if req.method == 'POST':
    data = {
      'book': book.pk,
      'text': req.data['text'],
    }
    serializer = CommentSerializer(data=data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response({"exception": "Failed to create comment"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def comments_all(req):
  try:
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  except Comment.DoesNotExist:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# only comments
@api_view(['GET', 'PUT', 'DELETE'])
def comment(req, pk):
  try:
    comment = Comment.objects.get(pk=pk) # get all the comments
  except Comment.DoesNotExist:
    return Response({'exception': 'Comment not found by Id {}'.format(pk)}, status=status.HTTP_404_NOT_FOUND)

  # requests
  if req.method == 'GET':
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  if req.method == 'PUT':
    serializer = CommentSerializer(comment, data=req.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if req.method == 'DELETE':
    comment.delete()
    return Response({'message': 'Comment by Id "{}" was successfully deleted'.format(pk)})