from api.models import Patient
from django.contrib import admin


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "is_confirmed",
        "email",
        "notify_appointment",
        "notify_pending_payment",
    )
