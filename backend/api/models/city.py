from api.constants.city import StateChoices
from api.models.base_model import Timestamp, Uuid
from django.db import models


class City(Uuid, Timestamp):
    name = models.CharField(max_length=32)
    state = models.CharField(max_length=4, choices=StateChoices.choices)

    def __str__(self) -> str:
        return f"{self.name}, {self.state}"
