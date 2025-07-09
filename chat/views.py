# chat/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import ChatRoom, ChatMessage

@login_required
def chat_list(request):
    # 현재 유저가 참여하고 있는 모든 채팅방을 가져옴
    chat_rooms = request.user.chat_rooms.all()
    
    # 각 채팅방에 대한 상대방 정보와 마지막 메시지를 담을 리스트
    rooms_with_details = []
    for room in chat_rooms:
        # 상대방 유저 찾기
        other_participant = room.participants.exclude(pk=request.user.pk).first()
        # 마지막 메시지 찾기
        last_message = room.messages.order_by('-timestamp').first()
        
        if other_participant:
            rooms_with_details.append({
                'room': room,
                'other_user': other_participant,
                'last_message': last_message,
            })

    # 마지막 메시지 시간을 기준으로 내림차순 정렬
    rooms_with_details.sort(
        key=lambda x: x['last_message'].timestamp if x['last_message'] else x['room'].created_at,
        reverse=True
    )

    context = {
        'chat_list': rooms_with_details
    }
    return render(request, 'chat/list.html', context)

@login_required
def search_user(request):
    if request.method == 'POST':
        username_to_search = request.POST.get('username', '').strip()
        if not username_to_search:
            messages.error(request, '아이디를 입력해주세요.')
            return redirect(reverse('home'))
        if username_to_search == request.user.username:
            messages.error(request, '자기 자신과는 채팅할 수 없습니다.')
            return redirect(reverse('home'))
        try:
            other_user = User.objects.get(username=username_to_search)
            return redirect(reverse('chat:chat_room', kwargs={'other_user_pk': other_user.pk}))
        except User.DoesNotExist:
            messages.error(request, f"'{username_to_search}' 사용자를 찾을 수 없습니다.")
            return redirect(reverse('home'))
    return redirect(reverse('home'))

@login_required
def chat_room(request, other_user_pk):
    if request.user.pk == other_user_pk:
        messages.error(request, '자기 자신과는 채팅할 수 없습니다.')
        return redirect(reverse('home'))

    other_user = get_object_or_404(User, pk=other_user_pk)
    
    # 두 유저가 참여하는 채팅방을 찾거나, 없으면 새로 생성
    room, created = ChatRoom.objects.get_or_create_by_participants(user1=request.user, user2=other_user)
    
    # 과거 메시지 불러오기
    past_messages = room.messages.all().order_by('timestamp')
    
    pks = sorted([request.user.pk, other_user.pk])
    room_name = f"{pks[0]}_{pks[1]}"

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'other_user': other_user,
        'past_messages': past_messages,
    })