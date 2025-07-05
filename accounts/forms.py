# accounts/forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['college', 'major', 'student_id', 'current_lifestyle', 'desired_lifestyle']
        widgets = {
            'current_lifestyle': forms.Textarea(attrs={'rows': 4, 'placeholder': '예: 아침형 인간, 주 3회 이상 운동, 야식 안 먹음'}),
            'desired_lifestyle': forms.Textarea(attrs={'rows': 4, 'placeholder': '예: 조용하고 잠이 많은 룸메이트 선호, 청결 중요, 주기적인 청소 원함'}),
        }
        labels = {
            'college': '단과대학',
            'major': '전공',
            'student_id': '학번',
            'current_lifestyle': '나의 현재 생활패턴',
            'desired_lifestyle': '내가 원하는 룸메이트 생활패턴',
        }