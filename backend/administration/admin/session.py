from api.models.session import Session
from django.contrib import admin


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "calendar",
        "week_day",
        "appointment",
        "is_scheduled",
    )
