import datetime
import json

import pytest
from api.models.calendar import Calendar
from django.urls import reverse

DEFAULT_TIME_FORMAT = "%H:%M:%S"


@pytest.mark.django_db
class TestCalendarViewSet:
    @staticmethod
    def test_calendar_with_slots_creation(
        admin_api, admin_profile, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        response = admin_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert str(calendar.profile.id) == str(admin_profile.id)
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.slots.count() == len(calendar_create_data["slots"])

        for dict_slot, slot in zip(calendar_create_data["slots"], calendar.slots.all()):
            time_start_string = slot.time_start.strftime(DEFAULT_TIME_FORMAT)
            time_finish_string = slot.time_finish.strftime(DEFAULT_TIME_FORMAT)

            assert dict_slot["time_start"] == time_start_string
            assert dict_slot["time_finish"] == time_finish_string

    @staticmethod
    def test_calendar_with_empty_slots_creation(
        admin_api, admin_profile, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        calendar_create_data["slots"] = []

        response = admin_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert str(calendar.profile.id) == str(admin_profile.id)
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.slots.count() == 0

    @staticmethod
    def test_calendar_without_slots_creation(
        admin_api, admin_profile, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        calendar_create_data.pop("slots")

        response = admin_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert str(calendar.profile.id) == str(admin_profile.id)
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.slots.count() == 0

    @staticmethod
    def test_calendar_with_slots_update(
        admin_api, admin_profile, calendar_create_data, calendar_update_data, slot
    ):
        url_post = reverse("api:calendar-list")

        print(calendar_create_data)
        response = admin_api.post(
            url_post, json.dumps(calendar_create_data), content_type="application/json"
        )

        calendar = Calendar.objects.first()

        url_patch = reverse("api:calendar-detail", kwargs={"pk": calendar.id})

        calendar_update_data["slots"].append(
            {
                "id": str(slot.id),
                "date": slot.date,
                "time_start": slot.time_start,
                "time_finish": slot.time_finish,
            }
        )

        response = admin_api.patch(
            url_patch, json.dumps(calendar_update_data), content_type="application/json"
        )

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert str(calendar.profile.id) == str(admin_profile.id)
        assert calendar.duration == calendar_update_data["duration"]
        assert calendar.is_default == calendar_update_data["is_default"]
        assert calendar.slots.count() == len(calendar_update_data["slots"])

        for dict_slot, slot in zip(calendar_update_data["slots"], calendar.slots.all()):
            time_start_string = slot.time_start.strftime(DEFAULT_TIME_FORMAT)
            time_finish_string = slot.time_finish.strftime(DEFAULT_TIME_FORMAT)

            assert dict_slot["time_start"] == time_start_string
            assert dict_slot["time_finish"] == time_finish_string

    @staticmethod
    def test_calendar_with_slots_on_creation_empty_on_update(
        admin_api, admin_profile, calendar_create_data, calendar_update_data
    ):
        url_post = reverse("api:calendar-list")

        response = admin_api.post(
            url_post, json.dumps(calendar_create_data), content_type="application/json"
        )

        calendar = Calendar.objects.first()

        url_patch = reverse("api:calendar-detail", kwargs={"pk": calendar.id})

        del calendar_update_data["slots"]

        response = admin_api.patch(
            url_patch, json.dumps(calendar_update_data), content_type="application/json"
        )

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert str(calendar.profile.id) == str(admin_profile.id)
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.slots.count() == len(calendar_create_data["slots"])

        for dict_slot, slot in zip(calendar_create_data["slots"], calendar.slots.all()):
            time_start_string = slot.time_start.strftime(DEFAULT_TIME_FORMAT)
            time_finish_string = slot.time_finish.strftime(DEFAULT_TIME_FORMAT)

            assert dict_slot["time_start"] == time_start_string
            assert dict_slot["time_finish"] == time_finish_string
