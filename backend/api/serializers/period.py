from rest_framework import serializers


class PeriodSerializer(serializers.Serializer):
    time_start = serializers.TimeField()
    time_end = serializers.TimeField()
    is_scheduled = serializers.BooleanField()

    class Meta:
        fields = (
            "time_start",
            "time_end",
            "is_scheduled",
        )


class AvailabilitySerializer(serializers.Serializer):
    periods = PeriodSerializer(many=True)

    def to_representation(self, instance):
        data = {}
        for day, periods in instance.items():
            period_data = PeriodSerializer(periods, many=True).data
            data[day] = period_data
        return data

    def to_internal_value(self, data):
        return data
