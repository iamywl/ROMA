# realll_match/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Profile, User
from django.db.models import Q

@login_required
def find_matches(request):
    try:
        current_user_profile = request.user.profile
    except Profile.DoesNotExist:
        return render(request, 'realll_match/matching_results.html', {'matches': []})

    other_users_profiles = Profile.objects.exclude(user=request.user)
    matches = []
    for other_profile in other_users_profiles:
        score = 0
        if current_user_profile.bedtime == other_profile.bedtime: score += 1
        if current_user_profile.wakeup_time == other_profile.wakeup_time: score += 1
        if current_user_profile.pref_smoking == 'N' and other_profile.smoking == 'N': score += 1
        if current_user_profile.pref_sleeping_habit == 'N' and other_profile.sleeping_habit == 'N': score += 1
        matches.append({'profile': other_profile, 'score': score})
    matches.sort(key=lambda x: x['score'], reverse=True)
    return render(request, 'realll_match/matching_results.html', {'matches': matches})