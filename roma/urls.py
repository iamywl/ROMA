# roma/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('init_roma.urls')),
    path('chat/', include('chat.urls')),
    path('realll_match/', include('realll_match.urls')), # <-- 이 줄을 추가하세요.
]