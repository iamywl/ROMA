# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import ChatRoom, ChatMessage
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if not self.user.is_authenticated:
            await self.close()
            return

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        # --- 읽음 처리 로직 추가 ---
        # 사용자가 연결되면, 이 방의 안 읽은 메시지를 읽음 처리
        await self.mark_messages_as_read()
        # 상대방에게 내 메시지들이 읽혔다고 알림
        await self.channel_layer.group_send(
            self.room_group_name,
            {'type': 'read_receipt'}
        )
        # --- 여기까지 추가 ---

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        chat_message = await self.save_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.user.username,
                'timestamp': chat_message.timestamp.isoformat()
            }
        )

    # --- 핸들러 추가 ---
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_message', # 메시지 타입을 명시
            'message': event['message'],
            'sender': event['sender'],
            'timestamp': event['timestamp']
        }))

    async def read_receipt(self, event):
        # "메시지 읽음" 이벤트를 클라이언트에게 전송
        await self.send(text_data=json.dumps({
            'type': 'read_receipt'
        }))
    # --- 여기까지 추가 ---

    @database_sync_to_async
    def save_message(self, message):
        user_pks = [int(pk) for pk in self.room_name.split('_')]
        user1 = User.objects.get(pk=user_pks[0])
        user2 = User.objects.get(pk=user_pks[1])
        room, created = ChatRoom.objects.get_or_create_by_participants(user1=user1, user2=user2)
        chat_message = ChatMessage.objects.create(room=room, sender=self.user, message=message)
        return chat_message

    # --- 읽음 처리 DB 업데이트 함수 추가 ---
    @database_sync_to_async
    def mark_messages_as_read(self):
        user_pks = [int(pk) for pk in self.room_name.split('_')]
        other_user_pk = user_pks[0] if user_pks[1] == self.user.pk else user_pks[1]
        other_user = User.objects.get(pk=other_user_pk)
        
        room, created = ChatRoom.objects.get_or_create_by_participants(user1=self.user, user2=other_user)
        
        # 이 방에서 상대방이 보낸, 아직 안 읽은 메시지들을 모두 읽음 처리
        room.messages.filter(sender=other_user, is_read=False).update(is_read=True)