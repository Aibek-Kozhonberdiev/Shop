from rest_framework import mixins, viewsets, permissions

from .models import Chat
from .serializers import ChatSerializer


class ChatView(mixins.RetrieveModelMixin,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               viewsets.GenericViewSet):
    queryset = Chat.objects.all().order_by('created_at', 'updated_at')
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Chat.objects.filter(users=self.request.user)


class MessageView(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'chat_id'

    def get_queryset(self):
        return Chat.objects.filter(users=self.request.user)
