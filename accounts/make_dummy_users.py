import random
from django.contrib.auth.models import User
from accounts.models import Profile

names = ['철수', '영희', '민수', '지수', '동욱', '세라', '진우', '수빈', '예린', '하늘', '태영', '은우', '현서', '소윤', '유진', '다은', '지환', '예준', '지안', '서윤']
colleges = ['공대', '인문대', '사회대', '예술대', '자연대']

GENDER_CHOICES = ['M', 'F']
BEDTIME_CHOICES = ['E', 'M', 'L', 'VL']
WAKEUP_CHOICES = ['E', 'M', 'L', 'VL']
HABIT_CHOICES = ['N', 'C', 'S']
DRYER_CHOICES = ['Y', 'N']
CALL_CHOICES = ['N', 'O']
LEVEL_CHOICES = ['L', 'M', 'H']
YES_NO_CHOICES = ['N', 'Y']
BUG_RESPONSE_CHOICES = ['C', 'M', 'P']
SNACK_CHOICES = ['O', 'S', 'N']
CLEANLINESS_CHOICES = ['O', 'M', 'L']
PREF_CHOICES_WITH_DONT_CARE = ['Y', 'N', 'D']
PREF_YES_NO_CHOICES = ['Y', 'N', 'D']
PREF_HABIT_CHOICES = ['Y', 'N', 'D']
PREF_RELATIONSHIP_CHOICES = ['F', 'M', 'B', 'D']

def rand_choice(arr):
    return random.choice(arr)

for i in range(100):
    username = f"testuser{i+1}"
    name = names[i % len(names)]
    college = rand_choice(colleges)
    gender = rand_choice(GENDER_CHOICES)
    bedtime = rand_choice(BEDTIME_CHOICES)
    wakeup_time = rand_choice(WAKEUP_CHOICES)
    sleeping_habit = rand_choice(HABIT_CHOICES)
    room_dryer = rand_choice(DRYER_CHOICES)
    in_room_call = rand_choice(CALL_CHOICES)
    heat_sensitivity = rand_choice(LEVEL_CHOICES)
    cold_sensitivity = rand_choice(LEVEL_CHOICES)
    smoking = rand_choice(YES_NO_CHOICES)
    bug_response = rand_choice(BUG_RESPONSE_CHOICES)
    late_night_snack = rand_choice(SNACK_CHOICES)
    cleaning_style = rand_choice(CLEANLINESS_CHOICES)

    # 룸메 선호
    pref_same_college = rand_choice(PREF_CHOICES_WITH_DONT_CARE)
    pref_bedtime = rand_choice(BEDTIME_CHOICES)
    pref_wakeup_time = rand_choice(WAKEUP_CHOICES)
    pref_sleeping_habit = rand_choice(PREF_HABIT_CHOICES)
    pref_in_room_call = rand_choice(CALL_CHOICES)
    pref_room_dryer = rand_choice(DRYER_CHOICES)
    pref_heat_sensitivity = rand_choice(LEVEL_CHOICES)
    pref_cold_sensitivity = rand_choice(LEVEL_CHOICES)
    pref_smoking = rand_choice(PREF_YES_NO_CHOICES)
    pref_bug_response = rand_choice(BUG_RESPONSE_CHOICES)
    pref_late_night_snack = rand_choice(SNACK_CHOICES)
    pref_cleaning_style = rand_choice(CLEANLINESS_CHOICES)
    pref_relationship = rand_choice(PREF_RELATIONSHIP_CHOICES)

    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password("1234")
        user.save()
    if not hasattr(user, 'profile'):
        profile = Profile.objects.create(user=user)
    else:
        profile = user.profile

    profile.name = name
    profile.college = college
    profile.gender = gender
    profile.bedtime = bedtime
    profile.wakeup_time = wakeup_time
    profile.sleeping_habit = sleeping_habit
    profile.room_dryer = room_dryer
    profile.in_room_call = in_room_call
    profile.heat_sensitivity = heat_sensitivity
    profile.cold_sensitivity = cold_sensitivity
    profile.smoking = smoking
    profile.bug_response = bug_response
    profile.late_night_snack = late_night_snack
    profile.cleaning_style = cleaning_style

    # 룸메 선호
    profile.pref_same_college = pref_same_college
    profile.pref_bedtime = pref_bedtime
    profile.pref_wakeup_time = pref_wakeup_time
    profile.pref_sleeping_habit = pref_sleeping_habit
    profile.pref_in_room_call = pref_in_room_call
    profile.pref_room_dryer = pref_room_dryer
    profile.pref_heat_sensitivity = pref_heat_sensitivity
    profile.pref_cold_sensitivity = pref_cold_sensitivity
    profile.pref_smoking = pref_smoking
    profile.pref_bug_response = pref_bug_response
    profile.pref_late_night_snack = pref_late_night_snack
    profile.pref_cleaning_style = pref_cleaning_style
    profile.pref_relationship = pref_relationship

    profile.save()

print("더미 유저 100명 자동 생성 완료")
