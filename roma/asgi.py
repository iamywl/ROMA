# roma/asgi.py (해결된 코드)
import os
from django.core.asgi import get_asgi_application

# 1. Django 설정 환경 변수를 먼저 설정합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roma.settings')

# 2. Django의 기본 ASGI 애플리케이션을 로드합니다.
#    이 과정에서 Django의 설정(settings.py)이 로드되고 초기화됩니다.
django_asgi_app = get_asgi_application()

# 3. Django 설정이 완료된 후에 Channels 관련 모듈과 우리 앱을 임포트합니다.
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,  # 위에서 로드한 변수를 사용
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})