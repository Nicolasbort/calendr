from api.models.calendar import Calendar
from api.models.session import Session
from api.serializers.generic import BaseSerializer
from rest_framework import serializers


class SessionSerializer(BaseSerializer):
    is_scheduled = serializers.ReadOnlyField()

    class Meta:
        model = Session
        depth = 1
        exclude = (
            "deleted_at",
            "calendar",
        )

    def save(self, **kwargs):
        request = self.context.get("request")
        default_calendar = Calendar.get_default(request.user.professional.id)

        return super().save(calendar=default_calendar)


class AppointmentSessionSerializer(BaseSerializer):
    is_scheduled = serializers.ReadOnlyField()

    class Meta:
        model = Session
        exclude = (
            "deleted_at",
            "calendar",
        )


class CalendarSessionSerializer(BaseSerializer):
    class Meta:
        model = Session
        fields = [
            "week_day",
            "time_start",
            "time_end",
        ]

    def validate(self, data):
        if data["time_start"] > data["time_end"]:
            raise serializers.ValidationError(
                {"time_end": "Ensure this value is greater than time_start"}
            )

        return data

    def create(self, validated_data):
        is_many = isinstance(validated_data, list)

        if is_many:
            return Session.objects.bulk_create(
                **validated_data,
                update_conflicts=True,
            )

        session, _ = Session.objects.update_or_create(**validated_data)

        return session
