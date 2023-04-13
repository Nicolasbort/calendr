import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestNotificationViewSet:
    @staticmethod
    def test_notification_read(professional_api, notification):
        assert notification.read_at is None

        url = reverse("api:notification-read", kwargs={"pk": notification.id})

        response = professional_api.post(url)

        assert response.status_code == 200

        response_data = response.json()

        notification.refresh_from_db()

        assert str(notification.id) == response_data["id"]
        assert notification.read_at is not None

    @staticmethod
    def test_notification_read_many(professional_api, notifications):
        for notification in notifications:
            assert notification.read_at is None

        url = reverse("api:notification-read-many")

        data = {"ids": [str(notification.id) for notification in notifications]}

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 204
