# init_roma/views.py (최신 버전)
from django.shortcuts import render

def home_page(request):
    # 홈페이지 템플릿을 화면에 보여주는 것이 최종 목표입니다.
    return render(request, 'init_roma/home_page.html')

# about_init_roma 뷰는 더 이상 사용하지 않으므로 삭제합니다.