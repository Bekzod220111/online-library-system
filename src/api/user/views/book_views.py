from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from api.user.serializers import book_serializers
from apps.book.models import Book
from rest_framework.permissions import IsAuthenticated


class BookListApiView(ListAPIView):
    serializer_class = book_serializers.BookListSeralzier
    queryset = Book.objects.all()
    


class BookCreateApiView(CreateAPIView):
    serializer_class = book_serializers.BookCreateSeralzier
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


class BookUpdateApiView(UpdateAPIView):
    serializer_class = book_serializers.BookUpdateSeralzier
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]



class BookDeleteApiView(DestroyAPIView):
    serializer_class = None
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
