from api.models.calendar import Calendar
from api.models.slot import Slot
from api.serializers.slot import SlotSerializer
from rest_framework import serializers


class CalendarSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, allow_empty=True, required=False)

    class Meta:
        model = Calendar
        read_only_fields = ["profile"]
        exclude = ("deleted_at", "is_deleted")

    def create(self, validated_data):
        request = self.context.get("request")
        slots = validated_data.pop("slots", [])
        is_default = validated_data.get("is_default", False)

        if is_default:
            # Remove the default calendar
            Calendar.objects.filter(profile=request.user, is_default=True).update(
                is_default=False
            )

        calendar = Calendar.objects.create(profile=request.user, **validated_data)

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
            Calendar.objects.filter(profile=request.user, is_default=True).update(
                is_default=False
            )

        return super().update(instance, validated_data)
