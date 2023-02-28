from functools import cached_property

from api.models.base_model import Timestamp, Uuid
from api.models.calendar import Calendar
from django.db import models


class CalendarEntry(Uuid, Timestamp):
    calendar = models.ForeignKey(
        Calendar, on_delete=models.CASCADE, related_name="entries", null=True
    )
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()

    @cached_property
    def duration(self) -> int:
        """
        Time in minutes of the calendar entry
        """
        diff = self.date_finish - self.date_start

        return round(diff.total_seconds() / 60)
