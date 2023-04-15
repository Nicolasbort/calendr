import logging

from api.models.calendar import Calendar
from api.models.session import Session
from api.serializers.generic import BaseSerializer, ReadOnlySerializer
from api.serializers.professional import ProfessionalSerializer
from api.serializers.session import CreateSessionSerializer, SessionSerializer
from api.utils.serializers import get_serialized_data

logger = logging.getLogger("django")


class CalendarSerializer(ReadOnlySerializer):
    professional = ProfessionalSerializer(read_only=True)
    sessions = SessionSerializer(many=True)

    class Meta:
        model = Calendar
        read_only_fields = (
            "professional",
            "sessions",
        )
        exclude = ("deleted_at",)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        session_serializer = SessionSerializer(
            data=instance.sessions.all().order_by("week_day", "time_start"), many=True
        )
        session_serializer.is_valid()

        data["sessions"] = session_serializer.data
        data["professional"] = get_serialized_data(
            ProfessionalSerializer, instance.professional
        )

        return data


class CreateCalendarSerializer(BaseSerializer):
    sessions = CreateSessionSerializer(many=True, allow_empty=True, required=False)

    class Meta:
        model = Calendar
        read_only_fields = ("professional",)
        exclude = ("deleted_at",)

    def create(self, validated_data):
        request = self.context.get("request")
        sessions = validated_data.pop("sessions", [])
        is_default = validated_data.get("is_default", False)

        if is_default:
            Calendar.unset_default(request.user.professional.id)

        calendar = Calendar.objects.create(
            professional=request.user.professional, **validated_data
        )

        session_serializer = CreateSessionSerializer(data=sessions, many=True)
        session_serializer.is_valid(raise_exception=True)
        calendar.sessions.set(session_serializer.save(calendar=calendar))

        return calendar

    def update(self, instance, validated_data):
        """
        Update will always override the sessions linked to the calendar IF, and only if,
        sessions are sent in the request. Otherwise the sessions will be ignored.
        """
        request = self.context.get("request")
        sessions = validated_data.pop("sessions", None)
        is_default = validated_data.get("is_default", False)

        if sessions is not None:
            instance.sessions.all().delete()

            for session in sessions:
                instance.sessions.add(Session(**session), bulk=False)

        if is_default:
            Calendar.unset_default(request.user.professional.id)

        return super().update(instance, validated_data)
