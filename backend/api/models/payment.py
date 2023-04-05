from api.models.appointment import Appointment
from api.models.base_model import BaseModel
from django.db import models


class Payment(BaseModel):
    appointment = models.ForeignKey(
        Appointment, on_delete=models.CASCADE, related_name="payments"
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
    partial = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Payment - {self.price}"
