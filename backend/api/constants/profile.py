from django.db import models


class GenreChoices(models.TextChoices):
    MALE = "M", "Masculino"
    FEMALE = "F", "Feminimo"
    OTHER = "O", "Outro"
