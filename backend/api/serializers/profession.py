from api.models.profession import Profession
from rest_framework import serializers


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = (
            "id",
            "name",
        )
