from api.models import Professional
from django.contrib import admin


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "plan",
        "genre",
    )
