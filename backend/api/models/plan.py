from functools import cache

from api.models.base_model import SoftDeletable, Timestamp, Uuid
from django.db import models


class Plan(Uuid, Timestamp, SoftDeletable):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return self.name

    @cache
    @staticmethod
    def get_free_plan():
        return Plan.objects.order_by("created_at").first()
