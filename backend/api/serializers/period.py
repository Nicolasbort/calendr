from rest_framework import serializers


class PeriodSerializer(serializers.Serializer):
    time_start = serializers.ReadOnlyField()
    time_end = serializers.ReadOnlyField()
