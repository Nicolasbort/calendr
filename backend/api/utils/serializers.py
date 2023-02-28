from django.db.models import Model
from rest_framework.serializers import ModelSerializer


def get_serialized_data(serializer: ModelSerializer, instance: Model) -> dict | None:
    return serializer(instance).data if instance else None
