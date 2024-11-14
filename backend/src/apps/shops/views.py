from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, filters
from django_filters import rest_framework

from .models import Shop
from .serializers import ShopSerializer


class ShopSetView(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['title', 'rating', 'create_to']
