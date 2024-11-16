import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Support
from .serializers import SupportSerializer


class SupportConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope.get('user')
        if user.is_superuser:
            await self.channel_layer.group_add("admin", self.channel_name)
            await self.accept()
            support_data = await self.get_objects()
            await self.send(text_data=json.dumps(support_data))
        else:
            await self.close()

    @database_sync_to_async
    def get_objects(self):
        support = Support.objects.all()
        serializer = SupportSerializer(support, many=True)
        return serializer.data
