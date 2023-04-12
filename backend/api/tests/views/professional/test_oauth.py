import json
from datetime import timedelta
from unittest.mock import patch

import pytest
from api.models.third_party import ThirdParty
from django.urls import reverse
from django.utils import timezone

EXPIRE_AT_FORMAT = "%Y-%m-%d %H:%M"


@pytest.mark.django_db
class TestOauthViewSet:
    @staticmethod
    def test_connect_google_calendar_missing_code(professional_api, professional):
        data = {}

        url = reverse("api:oauth-authorize")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 400

    @staticmethod
    @patch("api.services.google_calendar.GoogleCalendar.exchange_code")
    def test_connect_google_calendar(
        mock_exchange_code, professional_api, professional
    ):
        data = {"code": "random-google-oauth-code"}

        google_returned_data = {
            "access_token": "access-token",
            "refresh_token": "refresh-token",
            "scope": "",
            "expires_in": 3599,
        }

        mock_exchange_code.return_value = (True, google_returned_data)

        url = reverse("api:oauth-authorize")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        third_party = ThirdParty.objects.first()

        expire_at = timezone.now() + timedelta(
            seconds=google_returned_data["expires_in"]
        )
        expire_at = expire_at.strftime(EXPIRE_AT_FORMAT)

        assert third_party.professional.id == professional.id
        assert third_party.access_token == google_returned_data["access_token"]
        assert third_party.refresh_token == google_returned_data["refresh_token"]
        assert third_party.expire_at.strftime(EXPIRE_AT_FORMAT) == expire_at
        assert third_party.scopes == []

    @staticmethod
    @patch("api.services.google_calendar.GoogleCalendar.exchange_code")
    def test_connect_google_calendar_already_has_integration(
        mock_exchange_code, professional_api, professional, google_third_party
    ):
        data = {"code": "random-google-oauth-code"}

        google_returned_data = {
            "access_token": "new-access-token",
            "refresh_token": "new-refresh-token",
            "scope": "profile email",
            "expires_in": 4000,
        }

        mock_exchange_code.return_value = (True, google_returned_data)

        url = reverse("api:oauth-authorize")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200
        assert ThirdParty.objects.count() == 1

        google_third_party.refresh_from_db()

        expire_at = timezone.now() + timedelta(
            seconds=google_returned_data["expires_in"]
        )
        expire_at = expire_at.strftime(EXPIRE_AT_FORMAT)

        assert google_third_party.professional.id == professional.id
        assert google_third_party.access_token == google_returned_data["access_token"]
        assert google_third_party.refresh_token == google_returned_data["refresh_token"]
        assert google_third_party.expire_at.strftime(EXPIRE_AT_FORMAT) == expire_at
        assert google_third_party.scopes == ["profile", "email"]

    @staticmethod
    @patch("api.services.google_calendar.GoogleCalendar.exchange_code")
    def test_connect_google_calendar_invalid_code(
        mock_exchange_code, professional_api, professional
    ):
        data = {"code": "some-random-invalid-google-oauth-code"}

        google_returned_data = {"detail": "invalid_code", "message": "XXX"}

        mock_exchange_code.return_value = (False, google_returned_data)

        url = reverse("api:oauth-authorize")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 400
        assert ThirdParty.objects.count() == 0

        returned_data = response.json()

        assert returned_data == google_returned_data

    @staticmethod
    def test_connect_google_calendar_patient(patient_api):
        data = {"code": "some-random-invalid-google-oauth-code"}

        url = reverse("api:oauth-authorize")

        response = patient_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 403

    @staticmethod
    def test_connect_google_calendar_admin(admin_api):
        data = {"code": "some-random-invalid-google-oauth-code"}

        url = reverse("api:oauth-authorize")

        response = admin_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 403

    @staticmethod
    def test_connect_google_calendar_no_auth(no_auth_api):
        data = {"code": "some-random-invalid-google-oauth-code"}

        url = reverse("api:oauth-authorize")

        response = no_auth_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 401
