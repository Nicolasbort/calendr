from api.models.calendar import Calendar
from api.models.period import Period
from api.serializers.period import PeriodSerializer
from rest_framework import serializers


class CalendarSerializer(serializers.ModelSerializer):
    periods = PeriodSerializer(many=True, allow_empty=True, required=False)

    class Meta:
        model = Calendar
        fields = "__all__"

    def create(self, validated_data):
        periods = validated_data.pop("periods", [])

        calendar = Calendar.objects.create(**validated_data)

        for period in periods:
            calendar.periods.add(Period(**period), bulk=False)

        return calendar

    def update(self, instance, validated_data):
        """
        Update will always override the periods related to the calendar IF, and only if,
        periods are sent in the request. Otherwise the periods will be ignored.
        """
        periods = validated_data.pop("periods", None)

        if periods is not None:
            instance.periods.all().delete()

            for period in periods:
                instance.periods.add(Period(**period), bulk=False)

        return super().update(instance, validated_data)
