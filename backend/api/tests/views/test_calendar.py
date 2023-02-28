import json
from datetime import datetime

import pytest
from api.models.calendar import Calendar
from django.urls import reverse


@pytest.mark.django_db
class TestCalendarViewSet:
    @staticmethod
    def test_calendar_with_entries_creation(admin_api, calendar_create_data):
        url = reverse("api:calendar-list")

        response = admin_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert str(calendar.profile.id) == calendar_create_data["profile"]
        assert calendar.entries.count() == 4

        date_format = "%Y-%m-%d %H:%M:%S"

        for dict_entry, calendar_entry in zip(
            calendar_create_data["entries"], calendar.entries.all()
        ):
            date_start_string = calendar_entry.date_start.strftime(date_format)
            date_finish_string = calendar_entry.date_finish.strftime(date_format)

            assert dict_entry["date_start"] == date_start_string
            assert dict_entry["date_finish"] == date_finish_string

    @staticmethod
    def test_calendar_with_empty_entries_creation(admin_api, calendar_create_data):
        url = reverse("api:calendar-list")

        calendar_create_data["entries"] = []

        response = admin_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert str(calendar.profile.id) == calendar_create_data["profile"]
        assert calendar.entries.count() == 0

    @staticmethod
    def test_calendar_without_entries_creation(admin_api, calendar_create_data):
        url = reverse("api:calendar-list")

        calendar_create_data.pop("entries")

        response = admin_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert str(calendar.profile.id) == calendar_create_data["profile"]
        assert calendar.entries.count() == 0
