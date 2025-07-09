# chat/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class ChatRoomManager(models.Manager):
    def get_or_create_by_participants(self, user1, user2):
        """
        두 명의 참여자를 받아 채팅방을 찾거나 생성합니다.
        항상 동일한 채팅방을 반환하도록 보장합니다.
        """
        # 두 유저가 모두 참여한 채팅방을 찾습니다.
        # annotate와 filter를 사용하여 정확히 두 명만 있는 방을 찾습니다.
        room = self.annotate(num_participants=Count('participants')) \
                   .filter(num_participants=2) \
                   .filter(participants=user1) \
                   .filter(participants=user2) \
                   .first()
        
        created = False
        if not room:
            room = self.create()
            room.participants.add(user1, user2)
            created = True
        
        return room, created

class ChatRoom(models.Model):
    participants = models.ManyToManyField(User, related_name='chat_rooms', verbose_name='참여자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    objects = ChatRoomManager() # 커스텀 매니저 등록

    def __str__(self):
        usernames = ", ".join([user.username for user in self.participants.all()])
        return f"ChatRoom ({usernames})"

class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages', verbose_name='채팅방')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name='발신자')
    message = models.TextField(verbose_name='메시지 내용')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='전송 시간')
    is_read = models.BooleanField(default=False, verbose_name='읽음 여부')

    def __str__(self):
        return f"[{self.room}] {self.sender.username}: {self.message}"

    class Meta:
        ordering = ['timestamp']