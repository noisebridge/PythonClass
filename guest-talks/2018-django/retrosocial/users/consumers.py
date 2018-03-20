import json

from channels.generic.websocket import AsyncWebsocketConsumer


GROUP_NAME = 'default'


class FeedConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            group=GROUP_NAME,
            channel=self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            group=GROUP_NAME,
            channel=self.channel_name
        )

    async def update_feed(self, event):
        await self.send(json.dumps(event))
