from typing import TypedDict


class ExchangeCode(TypedDict):
    access_token: str
    refresh_token: str
    expires_in: int
    scope: str


class EventDateTime(TypedDict):
    dateTime: str
    timeZone: str


class EventAttendee(TypedDict):
    email: str
    responseStatus: str


class EventReminder(TypedDict):
    minutes: int
    method: str


class Event(TypedDict):
    id: str | None
    summary: str
    description: str
    start: EventDateTime
    end: EventDateTime
    attendees: list[EventAttendee]
    reminders: list[EventReminder]


class EventResponseSuccess(TypedDict):
    id: str
    htmlLink: str


class EventResponseError(TypedDict):
    status: int
    detail: str
