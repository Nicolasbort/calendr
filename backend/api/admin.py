from api.models import (
    Address,
    Appointment,
    Calendar,
    City,
    Patient,
    Payment,
    Plan,
    Profession,
    Professional,
    Profile,
    Slot,
)
from django.contrib import admin

admin.site.register(Address)
admin.site.register(Appointment)
admin.site.register(Calendar)
admin.site.register(Slot)
admin.site.register(City)
admin.site.register(Patient)
admin.site.register(Payment)
admin.site.register(Plan)
admin.site.register(Profession)
admin.site.register(Profile)
admin.site.register(Professional)
