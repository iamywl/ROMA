# roma/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # /accounts/ 요청은 accounts 앱으로
    path('', include('init_roma.urls')),        # 나머지 모든 요청은 init_roma 앱으로
]