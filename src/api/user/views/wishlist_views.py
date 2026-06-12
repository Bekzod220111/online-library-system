from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from api.user.serializers import wishlist_serializers
from apps.book.models import Wishlist
from rest_framework.permissions import IsAuthenticated


class WishlistListApiView(ListAPIView):
    serializer_class = wishlist_serializers.WishlistListSeralzier
    queryset = Wishlist.objects.all()
    


class WishlistCreateApiView(CreateAPIView):
    serializer_class = wishlist_serializers.WishlistCreateSeralzier
    queryset = Wishlist.objects.all()
    permission_classes = [IsAuthenticated]


class WishlistUpdateApiView(UpdateAPIView):
    serializer_class = wishlist_serializers.WishlistUpdateSeralzier
    queryset = Wishlist.objects.all()
    permission_classes = [IsAuthenticated]



class WishlistDeleteApiView(DestroyAPIView):
    serializer_class = None
    queryset = Wishlist.objects.all()
    permission_classes = [IsAuthenticated]
