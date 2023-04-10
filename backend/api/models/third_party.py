import builtins

from api.constants.third_party import ThirdPartyNameChoices
from api.models.base_model import Timestamp, Uuid
from api.models.professional import Professional
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class ThirdParty(Uuid, Timestamp):
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="third_parties",
    )
    name = models.CharField(max_length=32, choices=ThirdPartyNameChoices.choices)
    access_token = models.TextField()
    refresh_token = models.TextField(null=True)
    expire_at = models.DateTimeField(null=True)
    scopes = ArrayField(models.CharField(max_length=255), blank=True)

    @builtins.property
    def can_refresh(self) -> bool:
        return self.refresh_token is not None

    @builtins.property
    def is_expired(self) -> bool:
        now = timezone.now()

        return now >= self.expire_at

    @classmethod
    def get_professional_third_party_by_name(
        cls, professional_id: str, name: ThirdPartyNameChoices
    ) -> "ThirdParty":
        cls.objects.filter(professional=professional_id, name=name).first()

    class Meta:
        verbose_name_plural = "Third Parties"
