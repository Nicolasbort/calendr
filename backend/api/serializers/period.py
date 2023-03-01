from api.models.period import Period
from rest_framework import serializers


class PeriodSerializer(serializers.ModelSerializer):
    duration = serializers.ReadOnlyField()

    class Meta:
        model = Period
        fields = "__all__"

    def create(self, validated_data):
        is_many = isinstance(validated_data, list)

        if is_many:
            return Period.objects.bulk_create(
                **validated_data,
                update_conflicts=True,
            )

        return Period.objects.update_or_create(**validated_data)
