from django.db import models

from api.models.base_model import Timestamp, Uuid


class Profession(Uuid, Timestamp):
    name = models.CharField(max_length=32, unique=True)
