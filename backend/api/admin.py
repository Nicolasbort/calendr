from api.models import (
    Address,
    Appointment,
    Calendar,
    City,
    Patient,
    Payment,
    Period,
    Plan,
    Profession,
    Profile,
)
from django.contrib import admin

admin.site.register(Address)
admin.site.register(Appointment)
admin.site.register(Calendar)
admin.site.register(Period)
admin.site.register(City)
admin.site.register(Patient)
admin.site.register(Payment)
admin.site.register(Plan)
admin.site.register(Profession)
admin.site.register(Profile)
