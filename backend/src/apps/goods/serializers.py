from rest_framework import serializers

from .models import Product, ProductFoto, Category, SubCategory


class SerializerProduct(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class SerializerProductFoto(serializers.ModelSerializer):

    class Meta:
        model = ProductFoto
        fields = "__all__"


class SerializerCategory(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class SerializerSubCategory(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = "__all__"
