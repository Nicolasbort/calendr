import builtins

from api.constants.profile import GenreChoices
from api.models.address import Address
from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.plan import Plan
from api.models.profession import Profession
from api.models.profile import Profile
from django.db import models


class Professional(Uuid, Timestamp, SoftDeletable):
    profession = models.ForeignKey(
        Profession,
        on_delete=models.RESTRICT,
        related_name="professionals",
        db_index=True,
    )
    plan = models.ForeignKey(
        Plan, on_delete=models.RESTRICT, related_name="professioals", db_index=True
    )
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="professional", db_index=True
    )
    address = models.OneToOneField(Address, on_delete=models.RESTRICT, null=True)
    picture = models.CharField(max_length=128, null=True)
    genre = models.CharField(max_length=1, choices=GenreChoices.choices)
    birthday = models.DateField(null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.profile.full_name
