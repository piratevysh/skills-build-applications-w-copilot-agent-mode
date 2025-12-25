from rest_framework import viewsets
from . import models, serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = models.Workout.objects.all()
    serializer_class = serializers.WorkoutSerializer


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Leaderboard.objects.all().order_by('-score')
    serializer_class = serializers.LeaderboardSerializer
