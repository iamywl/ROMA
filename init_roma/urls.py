# ~/roma/init_roma/urls.py 파일 내용 (새로 생성)

from django.urls import path
from . import views # 현재 디렉토리(init_roma)의 views.py를 불러옵니다.

# urlpatterns 리스트에 URL 패턴을 정의합니다.
urlpatterns = [
    # path('', ...) : 'http://localhost:12345/init_roma/' 주소에 연결됩니다.
    path('', views.home_page, name='home_page_init_roma'),

    # path('about/', ...) : 'http://localhost:12345/init_roma/about/' 주소에 연결됩니다.
    path('about/', views.about_init_roma, name='about_page_init_roma'),
]
