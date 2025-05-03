from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import (
    RouteForm,
    ParticipantForm,
    ParticipantSkillLevelUpdateForm,
    ParticipantSearchForm,
    RouteSearchForm,
    TripSearchForm, TripForm,
)
from .models import Participant, Route, Trip


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ParticipantListView, self).get_context_data(**kwargs)
        last_name = self.request.GET.get("last_name")
        context["search_form"] = ParticipantSearchForm(
            initial={"last_name": last_name}
        )
        return context

    def get_queryset(self):
        queryset = Participant.objects.prefetch_related("trips")
        form = ParticipantSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                last_name__icontains=form.cleaned_data["last_name"]
            )
        return queryset


class ParticipantDetailView(LoginRequiredMixin, generic.DetailView):
    model = Participant
    queryset = Participant.objects.all().prefetch_related("trips__route")


class ParticipantCreateView(LoginRequiredMixin, generic.CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = "carpathians/participant_form.html"
    success_url = reverse_lazy("carpathians:participant-list")


class ParticipantSkillLevelUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Participant
    form_class = ParticipantSkillLevelUpdateForm
    success_url = reverse_lazy("carpathians:participant-list")


class ParticipantDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Participant
    template_name = "carpathians/participant_confirm_delete.html"
    success_url = reverse_lazy("carpathians:participant-list")


class RouteListView(LoginRequiredMixin, generic.ListView):
    model = Route
    template_name = "carpathians/route_list.html"
    context_object_name = "route_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RouteListView, self).get_context_data(**kwargs)
        start_point = self.request.GET.get("start_point", "")
        context["search_form"] = RouteSearchForm(
            initial={"start_point": start_point}
        )
        return context

    def get_queryset(self):
        queryset = Route.objects.select_related("difficulty")
        form = RouteSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            return queryset.filter(
                Q(start_point__icontains=query) | Q(end_point__icontains=query)
            )
        return queryset


class RouteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Route
    queryset = Route.objects.all().prefetch_related("trips__route")
    template_name = "carpathians/route_detail.html"
    context_object_name = "route_detail"


class RouteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Route
    form_class = RouteForm
    template_name = "carpathians/route_form.html"
    success_url = reverse_lazy("carpathians:route-list")


class RouteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Route
    form_class = RouteForm
    template_name = "carpathians/route_form.html"
    success_url = reverse_lazy("carpathians:route-list")


class RouteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Route
    template_name = "carpathians/route_confirm_delete.html"
    success_url = reverse_lazy("carpathians:route-list")


class TripListView(LoginRequiredMixin, generic.ListView):
    model = Trip
    paginate_by = 5
    queryset = Trip.objects.all().select_related("route")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.request.GET.get("date")
        context["search_form"] = TripSearchForm(initial={"date": date})
        return context

    def get_queryset(self):
        queryset = Trip.objects.all()
        form = TripSearchForm(self.request.GET)
        if form.is_valid():
            date = form.cleaned_data["date"]
            if date:
                queryset = queryset.filter(date=date)
        return queryset


class TripDetailView(LoginRequiredMixin, generic.DetailView):
    model = Trip
    template_name = "carpathians/trip_detail.html"
    context_object_name = "trip_detail"


class TripCreateView(LoginRequiredMixin, generic.CreateView):
    model = Trip
    form_class = TripForm
    template_name = "carpathians/trip_form.html"
    success_url = reverse_lazy("carpathians:trip-list")


class TripUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Trip
    form_class = TripForm
    template_name = "carpathians/trip_form.html"
    success_url = reverse_lazy("carpathians:trip-list")


class TripDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Trip
    template_name = "carpathians/trip_confirm_delete.html"
    success_url = reverse_lazy("carpathians:trip-list")


@login_required
def toggle_participation(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    user = request.user
    if user in trip.participants.all():
        trip.participants.remove(user)
    else:
        trip.participants.add(user)

    return redirect("carpathians:trip-detail", pk=trip.pk)
