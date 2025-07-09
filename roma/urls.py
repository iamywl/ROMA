# roma/urls.py
from django.contrib import admin
from django.urls import path, include  # include를 import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('init_roma.urls')),
    path('chat/', include('chat.urls')), # 이 줄을 추가!
]