from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Participant, SkillLevel, Route, Trip


@admin.register(Participant)
class ParticipantAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("skill_level",)
    fieldsets = UserAdmin.fieldsets + (
        ("Hiking Info", {"fields": ("skill_level",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Hiking Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "skill_level",
                )
            },
        ),
    )


@admin.register(SkillLevel)
class SkillLevelAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = (
        "start_point",
        "end_point",
        "distance_km",
        "duration_hours",
        "difficulty"
    )
    search_fields = ("start_point", "end_point")
    list_filter = ("difficulty",)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("date", "route_display")
    list_filter = ("date", "route__difficulty")
    search_fields = ("route__start_point", "route__end_point")

    def route_display(self, obj):
        return f"{obj.route.start_point} → {obj.route.end_point}"

    route_display.short_description = "Route"
