import json

import pytest
from api.models.calendar import Calendar
from api.models.session import Session
from django.urls import reverse

DEFAULT_TIME_FORMAT = "%H:%M:%S"


@pytest.mark.django_db
class TestCalendarViewSet:
    @staticmethod
    def test_create_calendar_with_sessions(
        professional_api, professional, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        response = professional_api.post(url, calendar_create_data)

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.is_active == calendar_create_data["is_active"]
        assert calendar.sessions.count() == len(calendar_create_data["sessions"])

        for dict_session, session in zip(
            calendar_create_data["sessions"], calendar.sessions.all()
        ):
            time_start_string = session.time_start.strftime(DEFAULT_TIME_FORMAT)
            time_end_string = session.time_end.strftime(DEFAULT_TIME_FORMAT)

            assert dict_session["time_start"] == time_start_string
            assert dict_session["time_end"] == time_end_string

    @staticmethod
    def test_create_calendar_sessions_invalid_time(
        professional_api, calendar_create_data_invalid_sessions
    ):
        url = reverse("api:calendar-list")

        response = professional_api.post(url, calendar_create_data_invalid_sessions)

        assert response.status_code == 400

        response_data = response.json()

        assert "sessions" in response_data
        assert len(response_data["sessions"]) == 3

        assert Calendar.objects.count() == 0
        assert Session.objects.count() == 0

    @staticmethod
    def test_create_calendar_with_sessions_atomic(
        professional_api, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        calendar_create_data["sessions"][0]["week_day"] = 99

        response = professional_api.post(url, calendar_create_data)

        assert response.status_code == 400

        assert Calendar.objects.count() == 0
        assert Session.objects.count() == 0

    @staticmethod
    def test_create_calendar_with_sessions_invalid_session_time_range(
        professional_api, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        calendar_create_data["sessions"][0]["time_start"] = "07:31:00"
        calendar_create_data["sessions"][0]["time_end"] = "07:30:00"

        response = professional_api.post(url, calendar_create_data)

        response_data = response.json()

        assert response.status_code == 400
        assert "sessions" in response_data

    @staticmethod
    def test_create_calendar_with_empty_sessions(
        professional_api, professional, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        calendar_create_data["sessions"] = []

        response = professional_api.post(url, calendar_create_data)

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.is_active == calendar_create_data["is_active"]
        assert calendar.sessions.count() == 0

    @staticmethod
    def test_create_calendar_without_sessions(
        professional_api, professional, calendar_create_data
    ):
        url = reverse("api:calendar-list")

        calendar_create_data.pop("sessions")

        response = professional_api.post(url, calendar_create_data)

        assert response.status_code == 201

        assert Calendar.objects.count() == 1

        calendar = Calendar.objects.first()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_create_data["duration"]
        assert calendar.is_default == calendar_create_data["is_default"]
        assert calendar.is_active == calendar_create_data["is_active"]
        assert calendar.sessions.count() == 0

    @staticmethod
    def test_update_calendar_with_sessions(
        professional_api,
        professional,
        session,
        calendar,
        calendar_update_data,
    ):
        url_patch = reverse("api:calendar-detail", kwargs={"pk": calendar.id})

        calendar_update_data["sessions"].append(
            {
                "id": str(session.id),
                "week_day": session.week_day,
                "time_start": session.time_start.strftime("%H:%M:%S"),
                "time_end": session.time_end.strftime("%H:%M:%S"),
            }
        )

        response = professional_api.patch(url_patch, calendar_update_data)

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_update_data["duration"]
        assert calendar.is_default == calendar_update_data["is_default"]
        assert calendar.is_active == calendar_update_data["is_active"]
        assert calendar.sessions.count() == len(calendar_update_data["sessions"])

        for dict_session, session in zip(
            calendar_update_data["sessions"], calendar.sessions.all()
        ):
            time_start_string = session.time_start.strftime(DEFAULT_TIME_FORMAT)
            time_end_string = session.time_end.strftime(DEFAULT_TIME_FORMAT)

            assert dict_session["time_start"] == time_start_string
            assert dict_session["time_end"] == time_end_string

    @staticmethod
    def test_update_calendar_without_sessions(
        professional_api,
        professional,
        calendar,
        calendar_update_data,
    ):
        count_calendar_sessions_before = calendar.sessions.count()

        url_patch = reverse("api:calendar-detail", kwargs={"pk": calendar.id})

        del calendar_update_data["sessions"]

        response = professional_api.patch(url_patch, calendar_update_data)

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert calendar.professional.id == professional.id
        assert calendar.duration == calendar_update_data["duration"]
        assert calendar.is_default == calendar_update_data["is_default"]
        assert calendar.is_active == calendar_update_data["is_active"]
        assert calendar.sessions.count() == count_calendar_sessions_before

    @staticmethod
    def test_update_calendar_other_professional_ignored(
        professional_api,
        professional,
        other_professional,
        calendar,
        calendar_update_data,
    ):
        url_patch = reverse("api:calendar-detail", kwargs={"pk": calendar.id})

        calendar_update_data["professional"] = str(other_professional.id)

        response = professional_api.patch(url_patch, calendar_update_data)

        assert response.status_code == 200

        calendar.refresh_from_db()

        assert calendar.professional.id == professional.id
