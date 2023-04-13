from api.models import City, Payment, Plan, Profession
from django.contrib import admin

from .address import *
from .appointment import *
from .calendar import *
from .patient import *
from .professional import *
from .profile import *
from .session import *

admin.site.register(City)
admin.site.register(Payment)
admin.site.register(Plan)
admin.site.register(Profession)
