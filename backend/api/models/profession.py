from api.models.base_model import SoftDeletable, Timestamp, Uuid
from django.db import models


class Profession(Uuid, Timestamp, SoftDeletable):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return self.name
