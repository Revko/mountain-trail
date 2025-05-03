from django.test import TestCase
from carpathians.models import Participant, Route, Trip, SkillLevel


class ModelsTest(TestCase):
    def test_participant_str(self):
        skill = SkillLevel.objects.create(name="Medium")
        participant = Participant.objects.create_user(
            username="sofiia123", first_name="Sofiia", last_name="Tkachenko",
            password="password", skill_level=skill
        )
        self.assertEqual(str(participant), "Tkachenko Sofiia (sofiia123)")

    def test_route_str(self):
        skill = SkillLevel.objects.create(name="Medium")
        route = Route.objects.create(
            start_point="Lviv", end_point="Ivano-Frankivsk", distance_km=150.5,
            duration_hours=3.5, difficulty=skill
        )
        self.assertEqual(str(route), "Lviv → Ivano-Frankivsk")

    def test_trip_str(self):
        skill = SkillLevel.objects.create(name="Hard")
        route = Route.objects.create(
            start_point="Kyiv",
            end_point="Uzhhorod",
            distance_km=350,
            duration_hours=5.5,
            difficulty=skill
        )
        trip = Trip.objects.create(date="2025-07-01", route=route)
        participant = Participant.objects.create_user(
            username="testuser",
            first_name="John",
            last_name="Doe",
            password="password",
            skill_level=skill
        )
        trip.participants.add(participant)

        self.assertEqual(str(trip), "Trip on 2025-07-01, Kyiv → Uzhhorod")
