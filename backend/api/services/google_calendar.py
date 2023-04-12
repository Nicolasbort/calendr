import json
from datetime import time
from typing import Tuple

import requests
from api.models.appointment import Appointment
from api.models.patient import Patient
from api.typings.google_calendar import (
    Event,
    EventResponseError,
    EventResponseSuccess,
    ExchangeCode,
)
from django.conf import settings


class GoogleCalendar:
    def __init__(self, access_token: str) -> None:
        self.API_URL = settings.GOOGLE_CALENDAR_API_URL
        self.EVENTS_URL = f"{self.API_URL}/primary/events"
        self.ACCESS_TOKEN = access_token
        self.TIMEZONE = "America/Sao_Paulo"

    def get_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

    def get_event_body(
        self,
        appointment: Appointment,
        summary: str,
        description: str,
        patients: list[Patient],
    ) -> Event:
        attendees = [
            {
                "email": patient.profile.email,
                "displayName": patient.full_name,
                "responseStatus": "needsAction",
            }
            for patient in patients
        ]

        return {
            "id": appointment.id,
            "summary": summary,
            "description": description,
            "start": {
                "dateTime": appointment.session.time_start.isoformat(),
                "timeZone": self.TIMEZONE,
            },
            "end": {
                "dateTime": appointment.session.time_end.isoformat(),
                "timeZone": self.TIMEZONE,
            },
            "attendees": attendees,
            "reminders": {
                "useDefault": False,
                "overrides": {
                    "minutes": 60,
                    "method": "email",
                },
            },
        }

    @classmethod
    def exchange_code(cls, code: str) -> Tuple[bool, ExchangeCode]:
        data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }

        response = requests.post(settings.GOOGLE_OAUTH_URL, data=data)

        if response.status_code == 200:
            return True, response.json()

        return False, response.json()

    def create_event(
        self,
        appointment: Appointment,
        summary: str,
        description: str,
        patients: list[Patient],
    ) -> Tuple[bool, EventResponseSuccess | EventResponseError]:
        event = self.get_event_body(appointment, summary, description, patients)

        response = requests.post(
            self.EVENTS_URL, headers=self.get_headers(), json=event
        )

        data = response.json()

        if response.status_code == 200:
            return True, data

        return False, {
            "status_code": response.status_code,
            "detail": data,
        }

    def update_event(
        self,
        appointment: Appointment,
        summary: str,
        description: str,
        attendees_emails: list[str],
    ) -> Tuple[bool, EventResponseSuccess | EventResponseError]:
        event = self.get_event_body(appointment, summary, description, attendees_emails)

        update_url = f"{self.EVENTS_URL}/{appointment.id}"
        response = requests.put(update_url, headers=self.get_headers(), json=event)

        data = response.json()

        if response.status_code == 200:
            return True, data

        return False, {
            "status": response.status_code,
            "detail": data,
        }

    def get_events(self, start_date: time, end_date: time):
        params = {
            "timeMin": start_date.isoformat() + "Z",
            "timeMax": end_date.isoformat() + "Z",
            "singleEvents": True,
            "orderBy": "startTime",
        }
        response = requests.get(
            self.EVENTS_URL, headers=self.get_events(), params=params
        )

        if response.status_code == 200:
            events = json.loads(response.text).get("items", [])

            if not events:
                print("No events found for this time range.")

            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                print(f'{event["summary"]} ({start})')
        else:
            print(f"An error occurred: {response.status_code}")
            events = None

        return events
