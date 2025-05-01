from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from .models import SkillLevel, Participant, Route, Trip


@login_required
def index(request):
    num_participants = Participant.objects.count()
    num_routes = Route.objects.count()
    num_trips = Trip.objects.count()

    context = {
        "num_participants": num_participants,
        "num_routes": num_routes,
        "num_trips": num_trips,
    }

    return render(request, "carpathians/index.html", context=context)


class ParticipantListView(LoginRequiredMixin, generic.ListView):
    model = Participant
    paginate_by = 5


class ParticipantDetailView(LoginRequiredMixin, generic.DetailView):
    model = Participant
    queryset = Participant.objects.all().prefetch_related("trips__route")


class RouteListView(LoginRequiredMixin, generic.ListView):
    model = Route
    template_name = "carpathians/route_list.html"
    context_object_name = "route_list"
    paginate_by = 5


class RouteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Route
    queryset = Route.objects.all().prefetch_related("trips__route")
    template_name = "carpathians/route_detail.html"
    context_object_name = "route_detail"


class TripListView(LoginRequiredMixin, generic.ListView):
    model = Trip
    paginate_by = 5
    queryset = Trip.objects.all().select_related("route")


class TripDetailView(LoginRequiredMixin, generic.DetailView):
    model = Trip
    template_name = "carpathians/trip_detail.html"
    context_object_name = "trip_detail"
