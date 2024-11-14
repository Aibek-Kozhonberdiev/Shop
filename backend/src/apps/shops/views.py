from rest_framework.viewsets import ModelViewSet
from  rest_framework import permissions

from .models import Shop
from .serializers import ShopSerializer


class ShopSetView(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
