from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from .utils import calc_match_score

class MatchingTestCase(TestCase):
    def setUp(self):
        # 유저 3명 생성 (Profile은 signals.py에서 자동 생성됨)
        user1 = User.objects.create_user(username='user1', password='testpass')
        user2 = User.objects.create_user(username='user2', password='testpass')
        user3 = User.objects.create_user(username='user3', password='testpass')

        # 이미 생성된 Profile 가져와서 값 세팅
        profile1 = user1.profile
        profile1.name = "A"
        profile1.college = "공대"
        profile1.bedtime = "E"
        profile1.smoking = "N"
        profile1.pref_same_college = "공대"
        profile1.pref_bedtime = "E"
        profile1.pref_smoking = "N"
        profile1.save()

        profile2 = user2.profile
        profile2.name = "B"
        profile2.college = "공대"
        profile2.bedtime = "E"
        profile2.smoking = "N"
        profile2.pref_same_college = "공대"
        profile2.pref_bedtime = "E"
        profile2.pref_smoking = "N"
        profile2.save()

        profile3 = user3.profile
        profile3.name = "C"
        profile3.college = "문과"
        profile3.bedtime = "L"
        profile3.smoking = "Y"
        profile3.pref_same_college = "문과"
        profile3.pref_bedtime = "L"
        profile3.pref_smoking = "Y"
        profile3.save()

    def test_match_score_exact(self):
        """user1과 user2는 완전 일치, user3은 완전 불일치"""
        user1 = User.objects.get(username='user1')
        user2 = User.objects.get(username='user2')
        user3 = User.objects.get(username='user3')

        profile1 = user1.profile
        profile2 = user2.profile
        profile3 = user3.profile

        score_12 = calc_match_score(profile1, profile2)
        score_13 = calc_match_score(profile1, profile3)

        print("user1 vs user2 score:", score_12)  # 디버그용
        print("user1 vs user3 score:", score_13)

        # 단과대 +2, 취침 +2, 흡연 +1 = 5점
        self.assertEqual(score_12, 5)
        # 모두 다름 = 0점
        self.assertEqual(score_13, 0)

    def test_match_score_partial(self):
        """user1과 user3: 흡연만 같게 세팅"""
        user1 = User.objects.get(username='user1')
        user3 = User.objects.get(username='user3')
        profile1 = user1.profile
        profile3 = user3.profile

        # 흡연만 같게 조정
        profile1.pref_same_college = "문과"
        profile1.pref_bedtime = "L"
        profile1.pref_smoking = "Y"
        profile1.save()
        profile3.smoking = "Y"
        profile3.college = "문과"
        profile3.bedtime = "L"
        profile3.save()

        score = calc_match_score(profile1, profile3)
        print("user1 vs user3 (흡연만 같음) score:", score)

        # 단과대 +2, 취침 +2, 흡연 +1 = 5점 (둘이 모두 일치)
        self.assertEqual(score, 5)
