import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestSessionDefaultViewSet:
    @staticmethod
    def test_get_sessions(professional_api, calendar, sessions):
        url = reverse("api:session-list")

        response = professional_api.get(url)

        assert response.status_code == 200
        assert response.json()["count"] == len(sessions)

    @staticmethod
    def test_get_sessions_not_default(
        professional_api, calendar_not_default, sessions_not_default
    ):
        url = reverse("api:session-list")

        response = professional_api.get(url)

        assert response.status_code == 200
        assert response.json()["count"] == 0
