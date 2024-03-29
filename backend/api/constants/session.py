from django.db import models


class WeekDayChoices(models.IntegerChoices):
    SUNDAY = 0, "Domingo"
    MONDAY = 1, "Segunda"
    TUESDAY = 2, "Terça"
    WEDNESDAY = 3, "Quarta"
    THURDAY = 4, "Quinta"
    FRIDAY = 5, "Sexta"
    SATURDAY = 6, "Sábado"

    @classmethod
    def to_python(cls, week_day: int) -> int:
        """
        Week day choices are in Javascript format, starting on Sunday = 0.
        Python starts the week on Monday = 0
        """
        return week_day - 1 if week_day > 0 else 6
