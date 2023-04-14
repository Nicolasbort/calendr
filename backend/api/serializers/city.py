from api.models.city import City
from api.serializers.generic import ReadOnlySerializer


class CitySerializer(ReadOnlySerializer):
    class Meta:
        model = City
        exclude = (
            "deleted_at",
            "created_at",
            "modified_at",
        )

    def create(self, validated_data):
        city, _ = City.objects.get_or_create(
            state=validated_data["state"],
            name=validated_data["name"],
            defaults=validated_data,
        )

        return city
