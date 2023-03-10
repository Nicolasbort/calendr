from api.models.slot import Slot
from rest_framework import serializers


class SlotSerializer(serializers.ModelSerializer):
    duration = serializers.ReadOnlyField()

    class Meta:
        model = Slot
        fields = "__all__"


class CalendarSlotSerializer(serializers.ModelSerializer):
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
