import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get room_key from the URL and extract the two handles
        self.room_key = self.scope['url_route']['kwargs']['room_key']
        handles = self.room_key.split('_')

        if not self.scope['user'].is_authenticated:
            await self.close()
            return

        self.my_handle = self.scope['user'].handle

        # Validate the current user is part of the room
        if self.my_handle not in handles:
            await self.close()
            return

        # Identify the other user in the room
        self.other_handle = handles[0] if handles[1] == self.my_handle else handles[1]
        self.room_group_name = f"chat_{self.room_key}"

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming WebSocket messages
        data = json.loads(text_data)
        content = data.get('message', '').strip()
        if not content:
            return

        # Add the message to the database
        other = await sync_to_async(User.objects.get)(handle=self.other_handle)
        await sync_to_async(Message.objects.create)(
            sender=self.scope['user'],
            receiver=other,
            content=content
        )

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': content,
                'sender': self.my_handle,
            }
        )

    async def chat_message(self, event):
        # Receive message from room group and send it over websocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))
