# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

# --- 선택지를 위한 상수 정의 ---
# '나'를 위한 선택지
GENDER_CHOICES = [('M', '남'), ('F', '여')]
YES_NO_CHOICES = [('N', '비흡연'), ('Y', '흡연')]
LEVEL_CHOICES = [('L', '적게 탐'), ('M', '중간'), ('H', '많이 탐')]
CLEANLINESS_CHOICES = [('O', '한번에'), ('M', '중간'), ('L', '더러울때')]
HABIT_CHOICES = [('N', '없음'), ('C', '이갈이'), ('S', '코골이')]
WAKEUP_CHOICES = [('E', '~6시'), ('M', '7-8시'), ('L', '9-10시'), ('VL', '11시~')]
BEDTIME_CHOICES = [('E', '8-10시'), ('M', '11-12시'), ('L', '자정-1시'), ('VL', '2시~')]
BUG_RESPONSE_CHOICES = [('C', '못잡음'), ('M', '중간'), ('P', '잘잡음')]
SNACK_CHOICES = [('O', '자주'), ('S', '가끔'), ('N', '안먹음')]
CALL_CHOICES = [('N', '상관X'), ('O', '밖에서만')]
DRYER_CHOICES = [('Y', 'O'), ('N', 'X')]

# --- '룸메는?'을 위한 선택지 ('상관없음' 추가) ---
PREF_CHOICES_WITH_DONT_CARE = [('Y', '선호'), ('N', '비선호'), ('D', '상관없음')]
PREF_YES_NO_CHOICES = [('Y', '흡연자'), ('N', '비흡연자'), ('D', '상관없음')]
PREF_HABIT_CHOICES = [('Y', '있어도 됨'), ('N', '없어야 함'), ('D', '상관없음')]
PREF_RELATIONSHIP_CHOICES = [('F', '짱친'), ('M', '중간'), ('B', '비즈니스'), ('D', '상관없음')]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # ================== 나는? (My Info) ==================
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='이름')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='성별')
    birth_year = models.CharField(max_length=4, null=True, blank=True, verbose_name='생년')
    college = models.CharField(max_length=100, null=True, blank=True, verbose_name='단과대학')
    major = models.CharField(max_length=100, null=True, blank=True, verbose_name='전공')
    mbti = models.CharField(max_length=4, null=True, blank=True, verbose_name='MBTI')
    
    bedtime = models.CharField(max_length=2, choices=BEDTIME_CHOICES, null=True, blank=True, verbose_name='취침시간')
    wakeup_time = models.CharField(max_length=2, choices=WAKEUP_CHOICES, null=True, blank=True, verbose_name='기상시간')
    sleeping_habit = models.CharField(max_length=1, choices=HABIT_CHOICES, null=True, blank=True, verbose_name='잠버릇')
    noise_sensitivity = models.CharField(max_length=100, null=True, blank=True, verbose_name='잠귀(밝기)')
    shower_time = models.CharField(max_length=20, null=True, blank=True, verbose_name='샤워시간')
    room_dryer = models.CharField(max_length=1, choices=DRYER_CHOICES, null=True, blank=True, verbose_name='방에서 드라이기')
    in_room_call = models.CharField(max_length=1, choices=CALL_CHOICES, null=True, blank=True, verbose_name='실내통화')
    heat_sensitivity = models.CharField(max_length=1, choices=LEVEL_CHOICES, null=True, blank=True, verbose_name='더위')
    cold_sensitivity = models.CharField(max_length=1, choices=LEVEL_CHOICES, null=True, blank=True, verbose_name='추위')
    perfume_usage = models.CharField(max_length=20, null=True, blank=True, verbose_name='향수')
    smoking = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True, verbose_name='흡연여부')
    bug_response = models.CharField(max_length=1, choices=BUG_RESPONSE_CHOICES, null=True, blank=True, verbose_name='벌레')
    late_night_snack = models.CharField(max_length=1, choices=SNACK_CHOICES, null=True, blank=True, verbose_name='야식')
    cleaning_style = models.CharField(max_length=1, choices=CLEANLINESS_CHOICES, null=True, blank=True, verbose_name='청소')
    
    # ================== 룸메는? (Roommate Preference) ==================
    pref_same_college = models.CharField(max_length=1, choices=PREF_CHOICES_WITH_DONT_CARE, null=True, blank=True, verbose_name='선호 단과대')
    pref_bedtime = models.CharField(max_length=2, choices=BEDTIME_CHOICES, null=True, blank=True, verbose_name='선호 취침시간')
    pref_wakeup_time = models.CharField(max_length=2, choices=WAKEUP_CHOICES, null=True, blank=True, verbose_name='선호 기상시간')
    pref_sleeping_habit = models.CharField(max_length=1, choices=PREF_HABIT_CHOICES, null=True, blank=True, verbose_name='선호 잠버릇')
    pref_in_room_call = models.CharField(max_length=1, choices=CALL_CHOICES, null=True, blank=True, verbose_name='선호 실내통화')
    pref_room_dryer = models.CharField(max_length=1, choices=DRYER_CHOICES, null=True, blank=True, verbose_name='선호 방에서 드라이기')
    pref_heat_sensitivity = models.CharField(max_length=1, choices=LEVEL_CHOICES, null=True, blank=True, verbose_name='선호 더위')
    pref_cold_sensitivity = models.CharField(max_length=1, choices=LEVEL_CHOICES, null=True, blank=True, verbose_name='선호 추위')
    pref_smoking = models.CharField(max_length=1, choices=PREF_YES_NO_CHOICES, null=True, blank=True, verbose_name='선호 흡연여부')
    pref_bug_response = models.CharField(max_length=1, choices=BUG_RESPONSE_CHOICES, null=True, blank=True, verbose_name='선호 벌레')
    pref_late_night_snack = models.CharField(max_length=1, choices=SNACK_CHOICES, null=True, blank=True, verbose_name='선호 야식')
    pref_cleaning_style = models.CharField(max_length=1, choices=CLEANLINESS_CHOICES, null=True, blank=True, verbose_name='선호 청소')
    pref_relationship = models.CharField(max_length=1, choices=PREF_RELATIONSHIP_CHOICES, null=True, blank=True, verbose_name='원하는 룸메 관계')

    def __str__(self):
        return f'{self.user.username} Profile'