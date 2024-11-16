from rest_framework import mixins, viewsets, permissions

from .models import Complain, Support
from .serializers import ComplainSerializer, SupportSerializer


class ComplainView(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupportView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    permission_classes = [permissions.IsAuthenticated]
