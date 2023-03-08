from django.db import models


class WeekDayChoices(models.IntegerChoices):
    SUNDAY = 0, "Domingo"
    MONDAY = 1, "Segunda"
    TUESDAY = 2, "Terça"
    WEDNESDAY = 3, "Quarta"
    THURDAY = 4, "Quinta"
    FRIDAY = 5, "Sexta"
    SATURDAY = 6, "Sábado"
