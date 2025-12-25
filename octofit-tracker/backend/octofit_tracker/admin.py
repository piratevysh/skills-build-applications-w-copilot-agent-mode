from django.contrib import admin
from . import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username",)


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("activity_type", "user", "duration_minutes", "timestamp")


@admin.register(models.Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("title", "duration_minutes")


@admin.register(models.Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ("user", "score", "period")
