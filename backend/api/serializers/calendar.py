from api.models.calendar import Calendar
from api.models.calendar_entry import CalendarEntry
from api.serializers.calendar_entry import CalendarEntrySerializer
from rest_framework import serializers


class CalendarSerializer(serializers.ModelSerializer):
    entries = CalendarEntrySerializer(many=True, allow_empty=True, required=False)

    class Meta:
        model = Calendar
        fields = "__all__"

    def create(self, validated_data):
        entries = validated_data.pop("entries", [])

        calendar = Calendar.objects.create(**validated_data)

        for entry in entries:
            calendar.entries.add(CalendarEntry(**entry), bulk=False)

        return calendar
