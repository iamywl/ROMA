# chat/urls.py
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # /chat/ -> 채팅 목록 페이지
    path('', views.chat_list, name='chat_list'),
    
    # /chat/search/ -> 사용자 검색 처리
    path('search/', views.search_user, name='search_user'),
    
    # /chat/<pk>/ -> 특정 채팅방
    path('<int:other_user_pk>/', views.chat_room, name='chat_room'),
]