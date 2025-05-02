from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Participant, Route, Trip


class ParticipantForm(UserCreationForm):
    class Meta:
        model = Participant
        fields = ("username", "first_name", "last_name", "email", "skill_level")


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
    class Meta:
        model = Trip
        fields = "__all__"


class TripSearchForm(forms.Form):
    date = forms.DateField(
        required=False,
        label="Date",
        widget=forms.DateInput(attrs={"type": "date", "placeholder": "YYYY-MM-DD"})
    )
