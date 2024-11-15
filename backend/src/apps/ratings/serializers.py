from rest_framework import serializers

from .models import RatingShop, RatingProduct


class RatingShopSerializer(serializers.ModelSerializer):
    created_to = serializers.DateTimeField(read_only=True)
    updated_to = serializers.DateTimeField(read_only=True)

    class Meta:
        model = RatingShop
        fints = "__all__"


class RatingProductSerializer(serializers.ModelSerializer):
    created_to = serializers.DateTimeField(read_only=True)
    updated_to = serializers.DateTimeField(read_only=True)

    class Meta:
        model = RatingProduct
        fints = "__all__"
