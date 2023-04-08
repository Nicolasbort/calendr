from datetime import datetime

from api.models.appointment import Appointment
from api.serializers.generic import BaseSerializer
from api.utils.datetime import diff
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class AppointmentSerializer(BaseSerializer):
    duration = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        read_only_fields = (
            "id",
            "professional",
            "duration",
            "created_at",
            "modified_at",
        )
        exclude = ("deleted_at",)

    def validate_time_end(self, time_end):
        time_start = self.initial_data.get("time_start")
        time_start = datetime.strptime(time_start, "%H:%M:%S").time()

        if time_end <= time_start:
            raise ValidationError("Ensure this value is greater than time_start")

        return time_end

    def validate(self, attrs):
        slot = attrs["slot"]
        time_end = attrs["time_end"]
        time_start = attrs["time_start"]

        if time_end > slot.time_end or time_start < slot.time_start:
            raise ValidationError(
                f"Ensure the appointment is between the slot time start and end"
            )

        calendar_duration = slot.calendar.duration
        appointment_duration = diff(time_start, time_end)

        if appointment_duration % calendar_duration != 0:
            raise ValidationError(
                f"Ensure the duration of the appointment is mulitple of {calendar_duration}"
            )

        return attrs

    def save(self, **kwargs):
        request = self.context.get("request")

        return super().save(professional=request.user.professional)
