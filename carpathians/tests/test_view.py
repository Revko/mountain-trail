from django.test import TestCase
from django.urls import reverse
from carpathians.models import Route, Trip, SkillLevel
from django.contrib.auth import get_user_model


class ViewsTest(TestCase):
    def setUp(self):
        self.skill_level = SkillLevel.objects.create(name="medium", order=1)

        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="pass12345",
            first_name="Oksana",
            last_name="Horishnya",
            email="oksana@example.com",
            skill_level=self.skill_level
        )

        self.route = Route.objects.create(
            start_point="Uzhok",
            end_point="Verkhovyna",
            distance_km=55.5,
            duration_hours=18.0,
            difficulty=self.skill_level
        )

        self.trip = Trip.objects.create(
            date="2025-09-01",
            route=self.route
        )
        self.trip.participants.set([self.user])

        self.client.login(username="testuser", password="pass12345")

    def test_trip_create_view(self):
        response = self.client.post(
            reverse("carpathians:trip-create"),
            {
                "date": "2025-10-01",
                "route": self.route.id,
                "participants": [self.user.id]
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Trip.objects.count(), 2)

    def test_route_list_view(self):
        response = self.client.get(reverse("carpathians:route-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Uzhok")
        self.assertContains(response, "Verkhovyna")

    def test_participant_detail_view(self):
        response = self.client.get(
            reverse("carpathians:participant-detail", args=[self.user.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Oksana")
