# realll_match/urls.py
from django.urls import path
from . import views

app_name = 'realll_match' # 최종 앱 이름

urlpatterns = [
    path('', views.find_matches, name='find_matches'),
]