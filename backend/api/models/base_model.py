from uuid import uuid4
from django.db import models


class SoftDeletable(models.Model):
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Uuid(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique=True)

    class Meta:
        abstract = True
