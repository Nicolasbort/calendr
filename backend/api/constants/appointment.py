from django.db import models


class TypeChoices(models.TextChoices):
    ONLINE = "online", "Online",
    PRESENTIAL = "presential", "Presencial"
