from datetime import timedelta

from api.constants.third_party import ThirdPartyNameChoices
from api.models.third_party import ThirdParty
from api.permissions import IsProfessional
from api.serializers.oauth import OauthSerializer
from api.serializers.third_party import ThirdPartySerializer
from api.services.google_calendar import GoogleCalendar
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


@extend_schema(request=OauthSerializer, responses=ThirdPartySerializer)
class OauthViewSet(viewsets.ViewSet):
    permission_classes = [IsProfessional]

    @action(methods=["POST"], detail=False, url_path="authorize")
    def authorize(self, request, **kwargs):
        code = request.data.get("code")

        if code is None:
            raise ValidationError("'code' is missing in the request")

        success, data = GoogleCalendar.exchange_code(code)

        if not success:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)

        access_token = data["access_token"]
        refresh_token = data["refresh_token"]
        expires_in = data["expires_in"]
        scopes = data["scope"].split(" ") if data.get("scope") else []

        now = timezone.now()
        expire_at = now + timedelta(seconds=expires_in)

        professional = self.request.user.professional
        third_party, _ = ThirdParty.objects.update_or_create(
            professional=professional,
            name=ThirdPartyNameChoices.GOOGLE_CALENDAR,
            defaults={
                "name": ThirdPartyNameChoices.GOOGLE_CALENDAR,
                "professional": professional,
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expire_at": expire_at,
                "scopes": scopes,
            },
        )

        return Response(
            status=status.HTTP_200_OK,
            data=ThirdPartySerializer(instance=third_party).data,
        )
