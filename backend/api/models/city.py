from django.db import models

from api.models.base_model import Timestamp, Uuid
from api.constants.city import StateChoices


class City(Uuid, Timestamp):
    name = models.CharField(max_length=32)
    state = models.CharField(max_length=4, choices=StateChoices.choices)
