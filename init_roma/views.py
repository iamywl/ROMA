# ~/roma/init_roma/views.py 파일 내용

from django.shortcuts import render
from django.http import HttpResponse

# 첫 번째 뷰: 홈페이지 내용을 반환합니다.
def home_page(request):
    """
    http://localhost:12345/init_roma/ 주소에 접속했을 때 보이는 페이지입니다.
    """
    return HttpResponse("<h1>환영합니다! init_roma 앱의 첫 페이지입니다!</h1><p>이것은 Python과 Django로 만든 웹페이지입니다.</p>")

# 두 번째 뷰: 소개 페이지 내용을 반환합니다.
def about_init_roma(request):
    """
    http://localhost:12345/init_roma/about/ 주소에 접속했을 때 보이는 페이지입니다.
    """
    return HttpResponse("<h2>init_roma 앱 소개</h2><p>이 앱은 Django 프로젝트의 초기 설정 및 기본 페이지를 담당합니다. 함께 성장해나가요!</p>")
