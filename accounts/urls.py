# accounts/urls.py
from django.urls import path
# Django의 내장 인증 뷰(auth_views)를 가져와야 합니다.
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    # --- 이 부분이 가장 중요합니다! ---
    # login 요청이 오면 auth_views.LoginView를 사용하도록 설정해야 합니다.
    # template_name으로 우리가 만든 login.html을 사용하라고 알려줍니다.
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my-page/', views.my_page, name='my_page'),
]