"""Populate octofit_db with test data using Django ORM.

Run this from the workspace with Python after installing requirements:

    python3 -m venv octofit-tracker/backend/venv
    source octofit-tracker/backend/venv/bin/activate
    pip install -r octofit-tracker/backend/requirements.txt
    python3 octofit-tracker/backend/scripts/populate_db.py

"""
import os
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(THIS_DIR, ".."))
sys.path.insert(0, BACKEND_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_settings")

import django
django.setup()

from octofit_tracker.models import UserProfile, Team, Activity


def populate():
    print("Populating octofit_db with test data...")
    Team.objects.all().delete()
    UserProfile.objects.all().delete()
    Activity.objects.all().delete()

    team_a = Team.objects.create(name="Team Alpha")
    team_b = Team.objects.create(name="Team Beta")

    alice = UserProfile.objects.create(username="alice", bio="Runner")
    bob = UserProfile.objects.create(username="bob", bio="Cyclist")

    Activity.objects.create(user=alice, team=team_a, activity_type="run", duration_minutes=35)
    Activity.objects.create(user=alice, team=team_a, activity_type="yoga", duration_minutes=20)
    Activity.objects.create(user=bob, team=team_b, activity_type="cycle", duration_minutes=60)

    print("Done.")


if __name__ == "__main__":
    populate()
