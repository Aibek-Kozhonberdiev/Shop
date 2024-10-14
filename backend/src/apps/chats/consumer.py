import json
from django.contrib.auth import get_user_model
from rest_framework import permissions
from channels.db import database_sync_to_async
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin, GenericAsyncAPIConsumer

from .models import Chat, Message
from .serializers import SerializerChat, SerializerMessage

User = get_user_model()


class ChatConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Chat.objects.all()
    serializer_class = SerializerChat
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = 'pk'

    async def connect(self):
        await self.accept()
        response = await self.get_catches()
        await self.send_json(response)

    async def receive_json(self, content, **kwargs):
        message_type = content.get('type')
        if message_type == 'send_message':
            await self.handle_send_message(content)
        elif message_type == 'create_chat':
            await self.handle_send_message(content)

    async def handle_send_message(self, content):
        serializer = SerializerMessage(data=json.loads(content.get('message')))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return await self.channel_layer.group_send(
                f"chat_{content.get('message', {}).get('chat_id')}",
                {
                    "type": "chat_message",
                    "message": serializer.data,
                }
            )
        await self.send_json(serializer.errors)

    async def handle_create_chat(self, content):
        response = await self.create_now_chat(content)
        await self.send_json(response)

    @database_sync_to_async
    def create_now_chat(self, content):
        serializer = SerializerChat(json.loads(content.get('data')))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return serializer.data
        return serializer.errors

    @database_sync_to_async
    def get_catches(self):
        chats = Chat.objects.filter(users=self.scope['user'])
        return SerializerChat(chats, many=True).data
