from api.models import Calendar
from django.contrib import admin


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = (
        "professional",
        "name",
        "duration",
        "interval",
        "is_default",
        "is_active",
    )
