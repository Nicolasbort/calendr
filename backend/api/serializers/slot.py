from api.models.slot import Slot
from api.serializers.generic import BaseSerializer
from rest_framework import serializers


class SlotSerializer(BaseSerializer):
    duration = serializers.IntegerField(read_only=True)

    class Meta:
        model = Slot
        fields = "__all__"


class CalendarSlotSerializer(BaseSerializer):
    class Meta:
        model = Slot
        fields = [
            "week_day",
            "time_start",
            "time_end",
        ]

    def create(self, validated_data):
        is_many = isinstance(validated_data, list)

        if is_many:
            return Slot.objects.bulk_create(
                **validated_data,
                update_conflicts=True,
            )

        return Slot.objects.update_or_create(**validated_data)
