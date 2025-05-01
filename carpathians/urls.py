from django.urls import path
from .views import (
    index,
    RouteListView,
    TripListView,
    ParticipantListView,
    ParticipantDetailView,
    TripDetailView,
    RouteDetailView,
)

app_name = "carpathians"

urlpatterns = [
    path("", index, name="index"),
    path("participant/", ParticipantListView.as_view(), name="participant-list"),
    path("participant/<int:pk>/", ParticipantDetailView.as_view(), name="participant-detail"),
    path("routes/", RouteListView.as_view(), name="route-list"),
    path("routes/<int:pk>/", RouteDetailView.as_view(), name="route-detail"),
    path("trips/", TripListView.as_view(), name="trip-list"),
    path("trips/<int:pk>/", TripDetailView.as_view(), name="trip-detail"),
]
