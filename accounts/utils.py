
def calc_match_score(my_profile, other_profile):
    score = 0

    # 선호 단과대
    if my_profile.pref_same_college and my_profile.pref_same_college != 'D':
        if other_profile.college and my_profile.pref_same_college == other_profile.college:
            score += 2

    # 선호 취침시간
    if my_profile.pref_bedtime and my_profile.pref_bedtime != 'D':
        if other_profile.bedtime and my_profile.pref_bedtime == other_profile.bedtime:
            score += 2

    # 선호 기상시간
    if my_profile.pref_wakeup_time and my_profile.pref_wakeup_time != 'D':
        if other_profile.wakeup_time and my_profile.pref_wakeup_time == other_profile.wakeup_time:
            score += 2

    # 선호 잠버릇
    if my_profile.pref_sleeping_habit and my_profile.pref_sleeping_habit != 'D':
        if other_profile.sleeping_habit and my_profile.pref_sleeping_habit == other_profile.sleeping_habit:
            score += 1

    # 선호 실내통화
    if my_profile.pref_in_room_call and my_profile.pref_in_room_call != 'D':
        if other_profile.in_room_call and my_profile.pref_in_room_call == other_profile.in_room_call:
            score += 1

    # 선호 드라이기
    if my_profile.pref_room_dryer and my_profile.pref_room_dryer != 'D':
        if other_profile.room_dryer and my_profile.pref_room_dryer == other_profile.room_dryer:
            score += 1

    # 선호 더위
    if my_profile.pref_heat_sensitivity and my_profile.pref_heat_sensitivity != 'D':
        if other_profile.heat_sensitivity and my_profile.pref_heat_sensitivity == other_profile.heat_sensitivity:
            score += 1

    # 선호 추위
    if my_profile.pref_cold_sensitivity and my_profile.pref_cold_sensitivity != 'D':
        if other_profile.cold_sensitivity and my_profile.pref_cold_sensitivity == other_profile.cold_sensitivity:
            score += 1

    # 선호 흡연
    if my_profile.pref_smoking and my_profile.pref_smoking != 'D':
        if other_profile.smoking and my_profile.pref_smoking == other_profile.smoking:
            score += 1

    # 선호 벌레
    if my_profile.pref_bug_response and my_profile.pref_bug_response != 'D':
        if other_profile.bug_response and my_profile.pref_bug_response == other_profile.bug_response:
            score += 1

    # 선호 야식
    if my_profile.pref_late_night_snack and my_profile.pref_late_night_snack != 'D':
        if other_profile.late_night_snack and my_profile.pref_late_night_snack == other_profile.late_night_snack:
            score += 1

    # 선호 청소
    if my_profile.pref_cleaning_style and my_profile.pref_cleaning_style != 'D':
        if other_profile.cleaning_style and my_profile.pref_cleaning_style == other_profile.cleaning_style:
            score += 1

    # 룸메 관계(참고용)
    if my_profile.pref_relationship and my_profile.pref_relationship != 'D':
        if other_profile.pref_relationship and my_profile.pref_relationship == other_profile.pref_relationship:
            score += 1

    return score
