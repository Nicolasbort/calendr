from rest_framework import serializers

from api.models.city import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
