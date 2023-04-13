from api.models import Professional
from django.contrib import admin


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "username",
        "email",
        "plan",
        "genre",
    )
