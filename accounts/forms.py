# accounts/forms.py
from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',) 

        widgets = {
            # '나는?' 섹션
            'gender': forms.RadioSelect,
            'bedtime': forms.RadioSelect,
            'wakeup_time': forms.RadioSelect,
            'sleeping_habit': forms.RadioSelect,
            'room_dryer': forms.RadioSelect,
            'in_room_call': forms.RadioSelect,
            'heat_sensitivity': forms.RadioSelect,
            'cold_sensitivity': forms.RadioSelect,
            'smoking': forms.RadioSelect,
            'bug_response': forms.RadioSelect,
            'late_night_snack': forms.RadioSelect,
            'cleaning_style': forms.RadioSelect,
            
            # '룸메는?' 섹션
            'pref_same_college': forms.RadioSelect,
            'pref_bedtime': forms.RadioSelect,
            'pref_wakeup_time': forms.RadioSelect,
            'pref_sleeping_habit': forms.RadioSelect,
            'pref_in_room_call': forms.RadioSelect,
            'pref_room_dryer': forms.RadioSelect,
            'pref_heat_sensitivity': forms.RadioSelect,
            'pref_cold_sensitivity': forms.RadioSelect,
            'pref_smoking': forms.RadioSelect,
            'pref_bug_response': forms.RadioSelect,
            'pref_late_night_snack': forms.RadioSelect,
            'pref_cleaning_style': forms.RadioSelect,
            'pref_relationship': forms.RadioSelect,
        }