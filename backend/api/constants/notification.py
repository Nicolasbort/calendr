from django.db import models


class TypeChoices(models.TextChoices):
    APPOINTMENT_CREATED = ("a-c", "Appointmet Created")
    APPOINTMENT_UPDATED = ("a-u", "Appointmet Updated")
