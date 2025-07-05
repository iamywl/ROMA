# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
# from .models import Profile # my_page 뷰 안에서 request.user.profile로 접근하므로 최상단 import는 불필요

# --- 회원가입 뷰 ---
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# --- 마이페이지 뷰 ---
@login_required
def my_page(request):
    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 성공적으로 업데이트되었습니다.')
            return redirect('my_page')
    else:
        form = ProfileForm(instance=profile)
        
    return render(request, 'accounts/my_page.html', {'form': form})