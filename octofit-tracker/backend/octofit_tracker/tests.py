import os
import sys
import django
from django.test import TestCase


class SmokeTest(TestCase):
    def test_create_sample(self):
        from .models import UserProfile, Team, Activity

        t = Team.objects.create(name="Testers")
        u = UserProfile.objects.create(username="alice")
        Activity.objects.create(user=u, team=t, activity_type="run", duration_minutes=30)

        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Activity.objects.count(), 1)
