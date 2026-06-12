from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from api.user.serializers import borrow_serializers
from apps.book.models import Borrow
from rest_framework.permissions import IsAuthenticated


class BorrowListApiView(ListAPIView):
    serializer_class = borrow_serializers.BorrowListSeralzier
    queryset = Borrow.objects.all()
    


class BorrowCreateApiView(CreateAPIView):
    serializer_class = borrow_serializers.BorrowCreateSeralzier
    queryset = Borrow.objects.all()
    permission_classes = [IsAuthenticated]


class BorrowUpdateApiView(UpdateAPIView):
    serializer_class = borrow_serializers.BorrowUpdateSeralzier
    queryset = Borrow.objects.all()
    permission_classes = [IsAuthenticated]



class BorrowDeleteApiView(DestroyAPIView):
    serializer_class = None
    queryset = Borrow.objects.all()
    permission_classes = [IsAuthenticated]
