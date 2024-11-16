from rest_framework import mixins, viewsets, permissions

from .models import Complain, SupportMessage
from .serializers import ComplainSerializer, SupportMessageSerializer


class ComplainView(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupportMessageView(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = SupportMessage.objects.all()
    serializer_class = SupportMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
