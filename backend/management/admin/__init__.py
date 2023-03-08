from api.models import City, Patient, Payment, Plan, Profession
from django.contrib import admin

from .address import *
from .appointment import *
from .calendar import *
from .professional import *
from .profile import *
from .slot import *

admin.site.register(City)
admin.site.register(Patient)
admin.site.register(Payment)
admin.site.register(Plan)
admin.site.register(Profession)
