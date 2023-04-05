from functools import cache

from api.models.base_model import BaseModel
from django.db import models


class Profession(BaseModel):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return self.name

    @cache
    @staticmethod
    def get_default_profession():
        return Profession.objects.order_by("created_at").first()
