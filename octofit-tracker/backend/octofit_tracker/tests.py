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


class ExtendedTest(TestCase):
    def test_workout_and_leaderboard(self):
        from .models import UserProfile, Team, Activity, Workout, Leaderboard

        t = Team.objects.create(name="TeamX")
        u = UserProfile.objects.create(username="charlie")
        Activity.objects.create(user=u, team=t, activity_type="swim", duration_minutes=45, distance_km=2.0)

        w = Workout.objects.create(title="Morning Run", description="Easy 5k", duration_minutes=30)
        lb = Leaderboard.objects.create(user=u, score=123.4, period="weekly")

        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(Leaderboard.objects.count(), 1)
