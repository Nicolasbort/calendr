import logging

from api.models.calendar import Calendar
from api.models.slot import Slot
from api.serializers.professional import ProfessionalSerializer
from api.serializers.slot import CalendarSlotSerializer, SlotSerializer
from api.services.slot import group_by_weekday
from api.utils.serializers import get_serialized_data
from rest_framework import serializers

logger = logging.getLogger("django")


class ListCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        exclude = ("deleted_at",)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        serializer = SlotSerializer(many=True, data=instance.slots)
        serializer.is_valid()

        data["slots"] = group_by_weekday(serializer.data)
        data["professional"] = get_serialized_data(
            ProfessionalSerializer, instance.professional
        )

        return data


class CalendarSerializer(serializers.ModelSerializer):
    slots = CalendarSlotSerializer(many=True, allow_empty=True, required=False)

    class Meta:
        model = Calendar
        read_only_fields = ["professional"]
        exclude = ("deleted_at",)

    def create(self, validated_data):
        request = self.context.get("request")
        slots = validated_data.pop("slots", [])
        is_default = validated_data.get("is_default", False)

        if is_default:
            # Remove the default calendar
            Calendar.objects.filter(
                professional=request.user.professional, is_default=True
            ).update(is_default=False)

        calendar = Calendar.objects.create(
            professional=request.user.professional, **validated_data
        )

        for slot in slots:
            calendar.slots.add(Slot(**slot), bulk=False)

        return calendar

    def update(self, instance, validated_data):
        """
        Update will always override the slots related to the calendar IF, and only if,
        slots are sent in the request. Otherwise the slots will be ignored.
        """
        request = self.context.get("request")
        slots = validated_data.pop("slots", None)
        is_default = validated_data.get("is_default", False)

        if slots is not None:
            instance.slots.all().delete()

            for slot in slots:
                instance.slots.add(Slot(**slot), bulk=False)

        if is_default:
            # Remove the default calendar
            Calendar.objects.filter(
                professional=request.user.professional, is_default=True
            ).update(is_default=False)

        return super().update(instance, validated_data)
