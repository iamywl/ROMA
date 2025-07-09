from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('my_page/', views.my_page, name='my_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),

    path('matching/start/', views.matching_start, name='matching_start'),
    path('matching/search/', views.matching_search, name='matching_search'),
    path('matching/result/', views.matching_result, name='matching_result'),
]
