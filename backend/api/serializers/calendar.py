from api.models.calendar import Calendar
from api.serializers.calendar_entry import CalendarEntrySerializer
from rest_framework import serializers


class CalendarSerializer(serializers.ModelSerializer):
    entries = CalendarEntrySerializer(many=True, required=False)

    class Meta:
        model = Calendar
        fields = ("profile", "entries")
