from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class SkillLevel(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(unique=True, default=0)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.name


class Participant(AbstractUser):
    skill_level = models.ForeignKey(SkillLevel, on_delete=models.SET_NULL, null=True, related_name="participants")

    class Meta:
        ordering = ("last_name",)

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.username})"

    def get_absolute_url(self):
        return reverse("carpathians:participant-detail", kwargs={"pk": self.pk})


class Route(models.Model):
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    distance_km = models.FloatField()
    duration_hours = models.FloatField()
    difficulty = models.ForeignKey(SkillLevel, on_delete=models.SET_NULL, null=True, related_name="routes")

    class Meta:
        ordering = ("start_point",)

    def __str__(self):
        return f"{self.start_point} → {self.end_point}"

    def get_absolute_url(self):
        return reverse("carpathians:route-detail", kwargs={"pk": self.pk})


class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="trips")
    date = models.DateField()
    participants = models.ManyToManyField(Participant, related_name="trips")

    class Meta:
        ordering = ("date",)

    def __str__(self):
        return f"Trip on {self.date} - {self.route}"

    def get_absolute_url(self):
        return reverse("carpathians:trip-detail", kwargs={"pk": self.pk})
