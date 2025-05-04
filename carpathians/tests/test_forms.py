from django.test import TestCase
from carpathians.forms import (
    ParticipantForm,
    ParticipantSkillLevelUpdateForm,
    ParticipantSearchForm,
    RouteForm,
    RouteSearchForm,
    TripForm,
    TripSearchForm
)
from carpathians.models import Participant, Route, SkillLevel


class ParticipantFormTest(TestCase):
    def setUp(self):
        self.skill_level = SkillLevel.objects.create(name="beginner", order=1)

    def test_participant_form_valid(self):
        form = ParticipantForm(data={
            "first_name": "Ivan",
            "last_name": "Shevchenko",
            "email": "ivan@example.com",
            "username": "ivanshevchenko",
            "password1": "SecurePassword123!",
            "password2": "SecurePassword123!",
            "skill_level": self.skill_level.id
        })

        self.assertTrue(form.is_valid())


class ParticipantSkillLevelUpdateFormTest(TestCase):
    def setUp(self):
        self.skill = SkillLevel.objects.create(name="Intermediate")
        self.participant = Participant.objects.create(
            first_name="Olena",
            last_name="Koval",
            email="olena@example.com",
            skill_level=self.skill,
            username="olenak",
            password="password123"
        )

    def test_skill_level_update_form_valid(self):
        form = ParticipantSkillLevelUpdateForm(
            data={"skill_level": self.skill.id}
        )
        self.assertTrue(form.is_valid())


class ParticipantSearchFormTest(TestCase):
    def test_search_form_valid(self):
        form = ParticipantSearchForm(data={"first_name": "Test"})
        self.assertTrue(form.is_valid())


class RouteFormTest(TestCase):
    def setUp(self):
        self.skill = SkillLevel.objects.create(name="Medium")

    def test_route_form_valid(self):
        form = RouteForm(data={
            "start_point": "Lviv",
            "end_point": "Kyiv",
            "distance_km": 150.0,
            "duration_hours": 3.0,
            "difficulty": self.skill.id
        })
        self.assertTrue(form.is_valid())


class RouteSearchFormTest(TestCase):
    def test_route_search_form_valid(self):
        form = RouteSearchForm(data={"name": "Pip Ivan"})
        self.assertTrue(form.is_valid())


class TripFormTest(TestCase):
    def setUp(self):
        self.skill = SkillLevel.objects.create(name="Hard")
        self.participant = Participant.objects.create(
            first_name="Mykola",
            last_name="Verbytskyi",
            email="mykola@example.com",
            skill_level=self.skill,
            username="mykola123",
            password="password123"
        )
        self.route = Route.objects.create(
            start_point="Chornohora",
            end_point="Beregovo",
            distance_km=120,
            duration_hours=3.5,
            difficulty=self.skill
        )

    def test_trip_form_valid(self):
        form = TripForm(data={
            "date": "2025-06-01",
            "participants": [self.participant.id],
            "route": self.route.id
        })
        self.assertTrue(form.is_valid())


class TripSearchFormTest(TestCase):
    def test_trip_search_form_valid(self):
        form = TripSearchForm(data={"route_name": "Gorgany"})
        self.assertTrue(form.is_valid())
