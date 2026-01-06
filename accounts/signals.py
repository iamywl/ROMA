# accounts/signals.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Profile 모델을 직접 임포트하는 대신, User 모델만 임포트합니다.
# User 모델은 settings.AUTH_USER_MODEL을 통해 가져오는 것이 더 안전합니다.
User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    User가 생성될 때 Profile을 생성하고,
    User가 저장될 때 Profile도 함께 저장합니다.
    """
    # Profile 모델을 함수가 호출되는 시점에 가져옵니다.
    from .models import Profile
    
    if created:
        Profile.objects.create(user=instance)
    
    instance.profile.save()