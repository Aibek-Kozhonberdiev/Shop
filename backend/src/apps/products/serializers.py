from decimal import Decimal

from rest_framework import serializers

from .models import Product, FotoProduct, Category, SubCategory


class FotoProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = FotoProduct
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    rating = serializers.DecimalField(read_only=True, max_digits=3, decimal_places=2, max_value=Decimal('5.00'), min_value=Decimal('0.00'))
    photos = FotoProductSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = "__all__"
