from rest_framework import serializers

from api.models.appointment import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = (
            "uuid",
            "created_at",
            "modified_at",
            "deleted_at",
            "profile",
        )

    def create(self, validated_data):
        request = self.context.get("request")

        return Appointment.objects.create(**validated_data, profile=request.user)
