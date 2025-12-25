from rest_framework import serializers
from . import models


class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = models.UserProfile
        fields = ["_id", "username", "bio"]


class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = models.Team
        fields = ["_id", "name"]


class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = models.Activity
        fields = ["_id", "user", "team", "activity_type", "duration_minutes", "distance_km", "calories", "timestamp"]


class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = models.Workout
        fields = ["_id", "title", "description", "duration_minutes"]


class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = models.Leaderboard
        fields = ["_id", "user", "score", "period"]
