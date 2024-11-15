from rest_framework import mixins, viewsets, permissions

from .models import RatingShop, RatingProduct
from .serializers import RatingShopSerializer, RatingProductSerializer


class RatingShopView(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = RatingShop.objects.all()
    serializer_class = RatingShopSerializer
    permission_classes = [permissions.IsAuthenticated]


class RatingProductView(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = RatingProduct.objects.all()
    serializer_class = RatingProductSerializer
    permission_classes = [permissions.IsAuthenticated]
