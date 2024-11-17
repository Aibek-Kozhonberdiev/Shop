from rest_framework import viewsets, permissions, filters
from rest_framework import mixins
from django_filters import rest_framework

from .models import Product, FotoProduct, SubCategory
from .serializers import ProductSerializer, FotoProductSerializer, SubCategorySerializer


class ProductSetView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('created_at', 'rating')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['title', 'rating', 'create_to', 'price', 'category']

    def get_queryset(self):
        return Product.objects.filter(shop__user__is_active=True)


class FotoProductSetView(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = FotoProduct.objects.all()
    serializer_class = FotoProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FotoProduct.objects.filter(product__shop__user=self.request.user)


class SubCategorySetView(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.AllowAny]
