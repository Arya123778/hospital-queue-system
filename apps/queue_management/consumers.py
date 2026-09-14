import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DoctorQueueConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.doctor_id = self.scope["url_route"]["kwargs"]["doctor_id"]
        self.room_group_name = f"doctor_queue_{self.doctor_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    # This handles messages broadcast to the group (called from services.py)
    async def queue_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))