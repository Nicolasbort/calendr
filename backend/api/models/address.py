from django.db import models

from api.models.base_model import Timestamp, Uuid


class Address(Uuid, Timestamp):
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=4)
    number = models.CharField(max_length=16)
    district = models.CharField(max_length=32, null=True, blank=True)
    complement = models.CharField(max_length=32, null=True, blank=True)
