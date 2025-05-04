from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Participant, Route, Trip


class ParticipantForm(UserCreationForm):
    class Meta:
        model = Participant
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "skill_level",
        )


class ParticipantSkillLevelUpdateForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ("skill_level",)


class ParticipantSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Last name",
        })
    )


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = "__all__"


class RouteSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Start or finish"
        })
    )


class TripForm(forms.ModelForm):
    route = forms.ModelChoiceField(
        queryset=Route.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label="Route"
    )

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        )
    )

    participants = forms.ModelMultipleChoiceField(
        queryset=Participant.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Participants"
    )

    class Meta:
        model = Trip
        fields = "__all__"


class TripSearchForm(forms.Form):
    date = forms.DateField(
        required=False,
        label="",
        widget=forms.DateInput(attrs={"type": "date", })
    )
