from rest_framework import serializers

from .models import RatingShop, RatingProduct, FotoRatingProduct


class RatingShopSerializer(serializers.ModelSerializer):
    created_to = serializers.DateTimeField(read_only=True)
    updated_to = serializers.DateTimeField(read_only=True)

    class Meta:
        model = RatingShop
        fields = "__all__"


class FotoRatingProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = FotoRatingProduct
        fields = "__all__"


class RatingProductSerializer(serializers.ModelSerializer):
    created_to = serializers.DateTimeField(read_only=True)
    updated_to = serializers.DateTimeField(read_only=True)
    photos = FotoRatingProductSerializer(read_only=True, many=True)

    class Meta:
        model = RatingProduct
        fields = "__all__"
