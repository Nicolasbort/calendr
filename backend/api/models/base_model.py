from uuid import uuid4

from django.db import models
from django.utils import timezone


class SoftDeletableQuerySet(models.query.QuerySet):
    def delete(self):
        self.update(deleted_at=timezone.now())

    def hard_delete(self):
        return super().delete()


class SoftDeleteManager(models.Manager):
    _queryset_class = SoftDeletableQuerySet

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)


class SoftDeletable(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False, soft=True):
        self.deleted_at = timezone.now()
        self.save(using=using)

    def hard_delete(self, using=None, keep_parents=False):
        return super().delete(using=using, keep_parents=keep_parents)

    def restore(self):
        self.deleted_at = None
        self.save()


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Uuid(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique=True)

    class Meta:
        abstract = True
