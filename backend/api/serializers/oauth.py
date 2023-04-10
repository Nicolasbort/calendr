from rest_framework import serializers


class OauthSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True)

    class Meta:
        fields = ("code",)
