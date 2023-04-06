import json

import pytest
from api.models.calendar import Calendar
from django.urls import reverse

DEFAULT_TIME_FORMAT = "%H:%M:%S"


@pytest.mark.django_db
class TestCalendarViewSet:
    @staticmethod
    def test_calendar_with_slots_creation(
        professional_api, professional, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        response = professional_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.is_active == calendar_create_data["is_active"]
        assert calendar.slots.count() == len(calendar_create_data["slots"])

        for dict_slot, slot in zip(calendar_create_data["slots"], calendar.slots.all()):
            time_start_string = slot.time_start.strftime(DEFAULT_TIME_FORMAT)
            time_end_string = slot.time_end.strftime(DEFAULT_TIME_FORMAT)

            assert dict_slot["time_start"] == time_start_string
            assert dict_slot["time_end"] == time_end_string

    @staticmethod
    def test_calendar_with_empty_slots_creation(
        professional_api, professional, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        calendar_create_data["slots"] = []

        response = professional_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.is_active == calendar_create_data["is_active"]
        assert calendar.slots.count() == 0

    @staticmethod
    def test_calendar_without_slots_creation(
        professional_api, professional, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        calendar_create_data.pop("slots")

        response = professional_api.post(
            url, json.dumps(calendar_create_data), content_type="application/json"
        )

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.is_active == calendar_create_data["is_active"]
        assert calendar.slots.count() == 0

    @staticmethod
    def test_calendar_with_slots_update(
        professional_api,
        professional,
        slot,
        calendar,
        calendar_update_data,
    ):
        url_patch = reverse(
            "api:calendar-detail", kwargs={"multiple_lookup_field": calendar.id}
        )

        calendar_update_data["slots"].append(
            {
                "id": str(slot.id),
                "week_day": slot.week_day,
                "time_start": slot.time_start.strftime("%H:%M:%S"),
                "time_end": slot.time_end.strftime("%H:%M:%S"),
            }
        )

        response = professional_api.patch(
            url_patch, json.dumps(calendar_update_data), content_type="application/json"
        )

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_update_data["duration"]
        assert calendar.is_default == calendar_update_data["is_default"]
        assert calendar.is_active == calendar_update_data["is_active"]
        assert calendar.slots.count() == len(calendar_update_data["slots"])

        for dict_slot, slot in zip(calendar_update_data["slots"], calendar.slots.all()):
            time_start_string = slot.time_start.strftime(DEFAULT_TIME_FORMAT)
            time_end_string = slot.time_end.strftime(DEFAULT_TIME_FORMAT)

            assert dict_slot["time_start"] == time_start_string
            assert dict_slot["time_end"] == time_end_string

    @staticmethod
    def test_calendar_with_slots_on_creation_empty_on_update(
        professional_api,
        professional,
        calendar_create_data,
        calendar_update_data,
    ):
        url_post = reverse("api:calendar-list")

        response = professional_api.post(
            url_post, json.dumps(calendar_create_data), content_type="application/json"
        )

        calendar = Calendar.objects.first()

        count_calendar_slots_before = calendar.slots.count()

        url_patch = reverse(
            "api:calendar-detail", kwargs={"multiple_lookup_field": calendar.id}
        )

        del calendar_update_data["slots"]

        response = professional_api.patch(
            url_patch, json.dumps(calendar_update_data), content_type="application/json"
        )

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_update_data["duration"]
        assert calendar.is_default == calendar_update_data["is_default"]
        assert calendar.is_active == calendar_update_data["is_active"]
        assert calendar.slots.count() == count_calendar_slots_before

    @staticmethod
    def test_calendar_update_professional_error(
        professional_api,
        professional,
        other_professional,
        calendar_create_data,
        calendar_update_data,
    ):
        url_post = reverse("api:calendar-list")

        response = professional_api.post(
            url_post, json.dumps(calendar_create_data), content_type="application/json"
        )

        calendar = Calendar.objects.first()

        url_patch = reverse(
            "api:calendar-detail", kwargs={"multiple_lookup_field": calendar.id}
        )

        calendar_update_data["professional"] = str(other_professional.id)

        response = professional_api.patch(
            url_patch, json.dumps(calendar_update_data), content_type="application/json"
        )

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert calendar.professional.id == professional.id

    @staticmethod
    def test_get_calendar_by_id(professional_api, calendar):
        url = reverse(
            "api:calendar-detail",
            kwargs={"multiple_lookup_field": calendar.id},
        )

        response = professional_api.get(url)

        assert response.status_code == 200

        returned_calendar = response.json()

        assert str(calendar.id) == returned_calendar["id"]
        assert str(calendar.professional.id) == returned_calendar["professional"]
        assert calendar.name == returned_calendar["name"]

    @staticmethod
    def test_get_calendar_by_username(professional_api, calendar):
        url = reverse(
            "api:calendar-detail",
            kwargs={"multiple_lookup_field": calendar.professional.profile.username},
        )

        response = professional_api.get(url)

        assert response.status_code == 200

        returned_calendar = response.json()

        assert str(calendar.id) == returned_calendar["id"]
        assert str(calendar.professional.id) == returned_calendar["professional"]
        assert calendar.name == returned_calendar["name"]

    @staticmethod
    def test_get_calendar_not_active(professional_api, calendar_not_active):
        url = reverse(
            "api:calendar-detail",
            kwargs={
                "multiple_lookup_field": calendar_not_active.professional.profile.username
            },
        )

        response = professional_api.get(url)

        assert response.status_code == 404

    @staticmethod
    def test_get_calendar_not_default(professional_api, calendar_not_default):
        url = reverse(
            "api:calendar-detail",
            kwargs={
                "multiple_lookup_field": calendar_not_default.professional.profile.username
            },
        )

        response = professional_api.get(url)

        assert response.status_code == 404

    @staticmethod
    def test_get_calendar_not_active_and_default(
        professional_api, calendar_not_active_and_default
    ):
        url = reverse(
            "api:calendar-detail",
            kwargs={
                "multiple_lookup_field": calendar_not_active_and_default.professional.profile.username
            },
        )

        response = professional_api.get(url)

        assert response.status_code == 404

    @staticmethod
    def test_get_calendar_by_id_not_active_and_default(
        professional_api, calendar_not_active_and_default
    ):
        url = reverse(
            "api:calendar-detail",
            kwargs={"multiple_lookup_field": calendar_not_active_and_default.id},
        )

        response = professional_api.get(url)

        assert response.status_code == 200
