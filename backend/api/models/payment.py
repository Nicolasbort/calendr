from django.db import models

from api.models.base_model import Timestamp, Uuid
from api.models.appointment import Appointment


class Payment(Uuid, Timestamp):
    appointment = models.ForeignKey(
        Appointment, on_delete=models.CASCADE, related_name="payments"
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
    partial = models.BooleanField(default=False)
