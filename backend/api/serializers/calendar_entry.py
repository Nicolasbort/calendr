from api.models.calendar_entry import CalendarEntry
from rest_framework import serializers


class CalendarEntrySerializer(serializers.ModelSerializer):
    duration = serializers.ReadOnlyField()

    class Meta:
        model = CalendarEntry
        fields = "__all__"
