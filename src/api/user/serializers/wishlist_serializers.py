from rest_framework.serializers import ModelSerializer
from apps.book.models import Wishlist


class WishlistCreateSeralzier(ModelSerializer):

    class Meta:
        model = Wishlist
        fields = '__all__'


class WishlistListSeralzier(ModelSerializer):

    class Meta:
        model = Wishlist
        fields = '__all__'


class WishlistUpdateSeralzier(ModelSerializer):

    class Meta:
        model = Wishlist
        fields = '__all__'