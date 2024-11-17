from decimal import Decimal

from rest_framework import serializers

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    rating = serializers.DecimalField(read_only=True, max_digits=3, decimal_places=2, max_value=Decimal('5.00'), min_value=Decimal('0.00'))

    class Meta:
        model = Shop
        fields = "__all__"
