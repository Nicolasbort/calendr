from django.db import models


class ThirdPartyNameChoices(models.TextChoices):
    GOOGLE_CALENDAR = "google-calendar", "Google Calendar"
