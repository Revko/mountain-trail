from django.test import TestCase
from carpathians.models import Participant, Route, Trip, SkillLevel
from carpathians.forms import (
    ParticipantSearchForm,
    RouteSearchForm,
    TripSearchForm
)
from datetime import date


class SearchFormTests(TestCase):
    def setUp(self):
        self.skill_level = SkillLevel.objects.create(name="easy", order=1)

        self.participant = Participant.objects.create(
            username="ivan123",
            first_name="Ivan",
            last_name="Franko",
            email="ivan@example.com",
            skill_level=self.skill_level
        )

        self.route = Route.objects.create(
            start_point="Kvasy",
            end_point="Hoverla peak",
            distance_km=15,
            duration_hours=6,
            difficulty=self.skill_level
        )

        self.trip = Trip.objects.create(
            date=date(2025, 9, 1),
            route=self.route
        )
        self.trip.participants.add(self.participant)

    def test_participant_search_form(self):
        form = ParticipantSearchForm(data={"last_name": "Franko"})
        self.assertTrue(form.is_valid())

    def test_route_search_form(self):
        form = RouteSearchForm(data={"query": "Hoverla"})
        self.assertTrue(form.is_valid())

    def test_trip_search_form(self):
        form = TripSearchForm(data={"date": "2025-09-01"})
        self.assertTrue(form.is_valid())
