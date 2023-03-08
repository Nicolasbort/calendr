from api.models import Slot
from django.contrib import admin


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = (
        "calendar",
        "week_day",
        "time_start",
        "time_end",
        "duration",
    )
