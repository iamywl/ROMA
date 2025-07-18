# chat/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # re_path는 정규 표현식을 사용하여 URL을 매칭합니다.
    # 채팅방의 ID(pk)를 URL 파라미터로 받아 consumer에게 전달합니다.
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]