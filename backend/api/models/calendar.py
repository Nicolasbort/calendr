from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.profile import Profile
from django.db import models


class Calendar(Uuid, Timestamp, SoftDeletable):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="calendar"
    )
