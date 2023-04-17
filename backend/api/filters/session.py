from functools import cached_property

from api.models.appointment import Appointment
from api.models.session import Session
from django.db.models import IntegerField, OuterRef, Subquery
from django_filters import DateFilter
from django_filters import rest_framework as filters
from django_filters.filters import OrderingFilter


class AppointmentField(IntegerField):
    def from_db_value(self, value, expression, connection):
        if value is not None:
            return Appointment.objects.get(pk=value)
        return value

    @cached_property
    def output_field(self):
        return AppointmentField()


class SessionFilter(filters.FilterSet):
    date = DateFilter(method="filter_date", label="Date")

    ordering = OrderingFilter(
        fields=(
            ("week_day", "week_day"),
            ("time_start", "time_start"),
        ),
        field_labels={
            "week_day": "Week day",
            "time_start": "Time start",
        },
    )

    class Meta:
        model = Session
        fields = ["date", "week_day"]

    def filter_date(self, queryset, name, value):
        week_day = value.weekday()

        appointment_subquery = Appointment.objects.filter(
            session=OuterRef("pk"),
            date=value,
        ).values("id")[:1]

        return queryset.filter(week_day=week_day).annotate(
            appointment=Subquery(
                appointment_subquery,
                output_field=AppointmentField(),
            )
        )
