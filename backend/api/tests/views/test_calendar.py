import json
from datetime import datetime

import pytest
from api.models.calendar import Calendar
from django.urls import reverse


@pytest.mark.django_db
class TestCalendarViewSet:
    @staticmethod
    def test_calendar_with_periods_creation(admin_api, calendar_create_data):
        url = reverse("api:calendar-list")

        response = admin_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert str(calendar.profile.id) == calendar_create_data["profile"]
        assert calendar.periods.count() == len(calendar_create_data["periods"])

        date_format = "%Y-%m-%d %H:%M:%S"

        for dict_period, period in zip(
            calendar_create_data["periods"], calendar.periods.all()
        ):
            date_start_string = period.date_start.strftime(date_format)
            date_finish_string = period.date_finish.strftime(date_format)

            assert dict_period["date_start"] == date_start_string
            assert dict_period["date_finish"] == date_finish_string

    @staticmethod
    def test_calendar_with_empty_periods_creation(admin_api, calendar_create_data):
        url = reverse("api:calendar-list")

        calendar_create_data["periods"] = []

        response = admin_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert str(calendar.profile.id) == calendar_create_data["profile"]
        assert calendar.periods.count() == 0

    @staticmethod
    def test_calendar_without_periods_creation(admin_api, calendar_create_data):
        url = reverse("api:calendar-list")

        calendar_create_data.pop("periods")

        response = admin_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert str(calendar.profile.id) == calendar_create_data["profile"]
        assert calendar.periods.count() == 0

    @staticmethod
    def test_calendar_with_periods_update(
        admin_api, calendar_create_data, calendar_update_data, period
    ):
        url_post = reverse("api:calendar-list")

        response = admin_api.post(
            url_post, json.dumps(calendar_create_data), content_type="application/json"
        )

        calendar = Calendar.objects.first()
        date_format = "%Y-%m-%d %H:%M:%S"

        url_patch = reverse("api:calendar-detail", kwargs={"pk": calendar.id})

        calendar_update_data["periods"].append(
            {
                "id": str(period.id),
                "date_start": period.date_start,
                "date_finish": period.date_finish,
            }
        )

        response = admin_api.patch(
            url_patch, json.dumps(calendar_update_data), content_type="application/json"
        )

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert str(calendar.profile.id) == calendar_update_data["profile"]
        assert calendar.periods.count() == len(calendar_update_data["periods"])

        for dict_period, period in zip(
            calendar_update_data["periods"], calendar.periods.all()
        ):
            date_start_string = period.date_start.strftime(date_format)
            date_finish_string = period.date_finish.strftime(date_format)

            assert dict_period["date_start"] == date_start_string
            assert dict_period["date_finish"] == date_finish_string

    @staticmethod
    def test_calendar_with_periods_on_creation_empty_on_update(
        admin_api, calendar_create_data, calendar_update_data
    ):
        url_post = reverse("api:calendar-list")

        response = admin_api.post(
            url_post, json.dumps(calendar_create_data), content_type="application/json"
        )

        calendar = Calendar.objects.first()

        url_patch = reverse("api:calendar-detail", kwargs={"pk": calendar.id})

        del calendar_update_data["periods"]

        response = admin_api.patch(
            url_patch, json.dumps(calendar_update_data), content_type="application/json"
        )

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert str(calendar.profile.id) == calendar_update_data["profile"]
        assert calendar.periods.count() == len(calendar_create_data["periods"])

        date_format = "%Y-%m-%d %H:%M:%S"

        for dict_period, period in zip(
            calendar_create_data["periods"], calendar.periods.all()
        ):
            date_start_string = period.date_start.strftime(date_format)
            date_finish_string = period.date_finish.strftime(date_format)

            assert dict_period["date_start"] == date_start_string
            assert dict_period["date_finish"] == date_finish_string
