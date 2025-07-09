from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from accounts.models import Profile
from accounts.utils import calc_match_score
from accounts.forms import ProfileUpdateForm

def home_page(request):
    return render(request, 'init_roma/home_page.html')

@login_required
def my_page(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_page')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'accounts/my_page.html', {'form': form})

@login_required
def matching_start(request):
    # 매칭 시작 페이지 (매칭 버튼만 있음)
    return render(request, 'init_roma/matching_start.html')

@login_required
def matching_search(request):
    # 매칭 중 대기 페이지
    return render(request, 'init_roma/matching_search.html')

@login_required
def matching_result(request):
    # 매칭 결과 페이지
    my_profile = request.user.profile
    others = Profile.objects.exclude(user=request.user)
    results = []
    for profile in others:
        score = calc_match_score(my_profile, profile)
        results.append({'profile': profile, 'score': score})
    results = sorted(results, key=lambda x: x['score'], reverse=True)[:5]
    return render(request, 'init_roma/matching_result.html', {'results': results})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/signup.html')
