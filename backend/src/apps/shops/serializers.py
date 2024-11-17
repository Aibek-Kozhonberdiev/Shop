from rest_framework import serializers

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Shop
        fields = "__all__"
