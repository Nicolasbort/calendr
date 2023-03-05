from api.models.profession import Profession
from rest_framework import serializers


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        exclude = ("deleted_at", "is_deleted")
