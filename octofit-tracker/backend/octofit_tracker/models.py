from djongo import models


class UserProfile(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="activities")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    activity_type = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} by {self.user} ({self.duration_minutes}m)"


class Workout(models.Model):
    """Predefined workout templates or suggestions."""
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Leaderboard(models.Model):
    """Snapshot entries for leaderboards (e.g., weekly top users)."""
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    score = models.FloatField()
    period = models.CharField(max_length=50, default="all-time")

    class Meta:
        indexes = [{"fields": ["-score"]}]

    def __str__(self):
        return f"{self.user}: {self.score} ({self.period})"
