from api.models.patient import Patient
from django.db.models import F, Value
from django.db.models.functions import Concat
from django_filters import CharFilter
from django_filters import rest_framework as filters


class PatientFilter(filters.FilterSet):
    name = CharFilter(method="filter_full_name", label="Name")

    class Meta:
        model = Patient
        fields = ["name"]

    def filter_full_name(self, queryset, name, value):
        return queryset.annotate(
            full_name=Concat(
                F("profile__first_name"), Value(" "), F("profile__last_name")
            )
        ).filter(full_name__icontains=value)
