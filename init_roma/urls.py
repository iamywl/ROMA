# init_roma/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    # path('about/', views.about_page, name='about'), # about 페이지는 나중에 추가
]