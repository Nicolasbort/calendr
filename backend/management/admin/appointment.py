from api.models import Appointment
from django.contrib import admin


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "professional",
        "patient",
        "time_start",
        "time_end",
        "price",
        "type",
    )
