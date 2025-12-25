import os
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from . import views


codespace_name = os.environ.get("CODESPACE_NAME")
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

router = routers.DefaultRouter()
router.register(r"users", views.UserProfileViewSet, basename="user")
router.register(r"teams", views.TeamViewSet, basename="team")
router.register(r"activities", views.ActivityViewSet, basename="activity")
router.register(r"workouts", views.WorkoutViewSet, basename="workout")
router.register(r"leaderboard", views.LeaderboardViewSet, basename="leaderboard")


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-list", request=request, format=format),
        "teams": reverse("team-list", request=request, format=format),
        "activities": reverse("activity-list", request=request, format=format),
        "workouts": reverse("workout-list", request=request, format=format),
        "leaderboard": reverse("leaderboard-list", request=request, format=format),
    })


urlpatterns = [
    path("", api_root, name="api-root"),
    path("api/", include(router.urls)),
]
