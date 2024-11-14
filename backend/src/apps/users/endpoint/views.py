from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from ..serializers import SetUserSerializer

User = get_user_model()


class UserSetView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = SetUserSerializer
    queryset = User.objects.all()
