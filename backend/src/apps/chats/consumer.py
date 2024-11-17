import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer

from .models import Chat
from .serializers import MessageSerializer


class MessageConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        chat_is = await self.check_chat(self.chat_id)
        if user.is_authenticated and chat_is:
            await self.channel_layer.group_add(self.chat_id, self.channel_name)
            await self.accept()
        else:
            await self.send_json(content={'detail': "Not fount."})
            await self.close()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.chat_id,
            self.channel_name
        )

    async def receive_json(self, content, **kwargs):
        content = json.dumps(content)
        message = await self.get_message(content)
        await self.channel_layer.group_send(
            f"chat_{self.chat_id}",
            {
                "type": "chat_message",
                "message": message
            }
        )

    async def send_message(self, event):
        message = event['message']
        await self.send_json(content=message)

    @database_sync_to_async
    async def check_chat(self, chat_id):
        try:
            return Chat.objects.get(pk=chat_id)
        except Chat.DoesNotExist:
            return False

    @database_sync_to_async
    async def get_message(self, content):
        serializer = MessageSerializer(content)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return serializer.data
        else:
            return serializer.errors


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if self.user.is_authenticated:
            await self.channel_layer.group_add(f"user_{self.user.id}", self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            f"user_{self.user.id}",
            self.channel_name
        )

    async def order_status(self, event):
        message = event['massage']
        await self.send(text_data=json.loads(message))
