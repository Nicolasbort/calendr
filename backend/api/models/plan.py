from api.models.base_model import BaseModel
from django.db import models


class Plan(BaseModel):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_free_plan():
        return Plan.objects.order_by("created_at").first()
