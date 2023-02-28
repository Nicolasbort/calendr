from api.models.base_model import Timestamp, Uuid
from api.models.city import City
from django.db import models


class Address(Uuid, Timestamp):
    street = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="addresses")
    number = models.CharField(max_length=16)
    district = models.CharField(max_length=32, null=True, blank=True)
    complement = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.street}, {self.number}, {self.district}"
