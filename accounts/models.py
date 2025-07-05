# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 기존 User 모델과 1:1 연결
    
    # 개인 정보
    college = models.CharField(max_length=100, blank=True, verbose_name='단과대학')
    major = models.CharField(max_length=100, blank=True, verbose_name='전공')
    student_id = models.CharField(max_length=20, blank=True, verbose_name='학번')
    
    # 기숙사 생활 패턴
    current_lifestyle = models.TextField(blank=True, verbose_name='현재 생활패턴')
    desired_lifestyle = models.TextField(blank=True, verbose_name='원하는 생활패턴')

    def __str__(self):
        return f'{self.user.username} Profile'