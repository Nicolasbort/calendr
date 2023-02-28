from api.models.patient import Patient
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = (
            "uuid",
            "created_at",
            "modified_at",
            "profile",
        )

    def create(self, validated_data):
        request = self.context.get("request")

        return Patient.objects.create(**validated_data, profile=request.user)
