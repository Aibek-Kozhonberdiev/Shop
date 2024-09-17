from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from .serializers import SerializerSetUser

User = get_user_model()


class UserVieSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = SerializerSetUser
    queryset = User.objects.all()
    pagination_class = None


def auth():
    pass


def logout():
    pass
