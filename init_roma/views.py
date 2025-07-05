# init_roma/views.py
from django.shortcuts import render

def home_page(request):
    return render(request, 'init_roma/home_page.html')