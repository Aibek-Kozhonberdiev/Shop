import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ComplaintConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        self.group = "admin"
        if user.is_superuser:
            await self.channel_layer.group_add(self.group, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group,
            self.channel_name
        )

    async def order_status(self, event):
        await self.send(text_data=json.dumps({
            'order_id': event['order_id'],
            'status': event['status'],
        }))
