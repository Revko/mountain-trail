from django.urls import path
from .views import (
    index,
    RouteListView,
    TripListView,
    ParticipantListView,
    ParticipantDetailView,
    TripDetailView,
    RouteDetailView,
    ParticipantCreateView,
    ParticipantSkillLevelUpdateView,
    ParticipantDeleteView,
    TripCreateView,
    TripUpdateView,
    TripDeleteView,
    RouteCreateView,
    RouteUpdateView,
    RouteDeleteView,
)

app_name = "carpathians"

urlpatterns = [
    path("", index, name="index"),
    path("participant/", ParticipantListView.as_view(), name="participant-list"),
    path("participant/<int:pk>/", ParticipantDetailView.as_view(), name="participant-detail"),
    path("participants/create/", ParticipantCreateView.as_view(), name="participant-create"),
    path("participants/<int:pk>/update/", ParticipantSkillLevelUpdateView.as_view(), name="participant-update"),
    path("participants/<int:pk>/delete/", ParticipantDeleteView.as_view(), name="participant-delete"),
    path("routes/", RouteListView.as_view(), name="route-list"),
    path("routes/<int:pk>/", RouteDetailView.as_view(), name="route-detail"),
    path("routes/create/", RouteCreateView.as_view(), name="route-create"),
    path("routes/<int:pk>/update/", RouteUpdateView.as_view(), name="route-update"),
    path("routes/<int:pk>/delete/", RouteDeleteView.as_view(), name="route-delete"),
    path("trips/", TripListView.as_view(), name="trip-list"),
    path("trips/<int:pk>/", TripDetailView.as_view(), name="trip-detail"),
    path("trips/create/", TripCreateView.as_view(), name="trip-create"),
    path("trips/<int:pk>/update/", TripUpdateView.as_view(), name="trip-update"),
    path("trips/<int:pk>/delete/", TripDeleteView.as_view(), name="trip-delete"),
]
