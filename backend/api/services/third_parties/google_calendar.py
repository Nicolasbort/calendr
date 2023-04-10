import json
from datetime import time
from typing import Union

import requests
from django.conf import settings


class GoogleCalendar:
    def __init__(self, access_token: str) -> None:
        self.API_URL = settings.GOOGLE_CALENDAR_API_URL
        self.EVENTS_URL = f"{self.API_URL}/primary/events"
        self.ACCESS_TOKEN = access_token

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

    def get_event_body(
        self,
        start_time: time,
        end_time: time,
        summary: str,
        description: str,
        attendees_emails: list[str],
    ):
        attendees = [
            {"email": email, "responseStatus": "needsAction"}
            for email in attendees_emails
        ]

        return {
            "summary": summary,
            "description": description,
            "start": {
                "dateTime": start_time.isoformat(),
                "timeZone": "UTC",
            },
            "end": {
                "dateTime": end_time.isoformat(),
                "timeZone": "UTC",
            },
            "attendees": attendees,
        }

    @classmethod
    def exchange_code(cls, code: str) -> Union[bool, dict]:
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
        start_time: time,
        end_time: time,
        summary: str,
        description: str,
        attendees_emails: list[str],
    ) -> Union[bool, dict]:
        event = self.get_event_body(
            start_time, end_time, summary, description, attendees_emails
        )

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
        event_id: str,
        start_time: time,
        end_time: time,
        summary: str,
        description: str,
        attendees_emails: list[str],
    ) -> Union[bool, dict]:
        event = self.get_event_body(
            start_time, end_time, summary, description, attendees_emails
        )

        update_url = f"{self.EVENTS_URL}/{event_id}"
        response = requests.put(update_url, headers=self.get_headers(), json=event)

        data = response.json()

        if response.status_code == 200:
            return True, data

        return False, {
            "status_code": response.status_code,
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
