from api.models.functions.levenshtein import Levenshtein
from api.models.patient import Patient
from django.db.models import F, Q
from django.db.models.functions import Lower
from django_filters import CharFilter
from django_filters import rest_framework as filters


class PatientFilter(filters.FilterSet):
    name = CharFilter(method="filter_full_name", label="Name")

    class Meta:
        model = Patient
        fields = ["name"]

    def filter_full_name(self, queryset, name, value):
        splited_value = value.lower().split(" ")
        first_name = splited_value[0]
        last_name = splited_value[-1] if len(splited_value) > 1 else None

        if last_name is not None:
            return (
                queryset.annotate(
                    first_name_dist=Levenshtein(
                        Lower(F("profile__first_name")),
                        first_name,
                    ),
                    last_name_dist=Levenshtein(
                        Lower(F("profile__last_name")),
                        last_name,
                    ),
                )
                .filter(Q(first_name_dist__lte=5) | Q(last_name_dist__lte=5))
                .order_by("first_name_dist", "last_name_dist")
            )

        return (
            queryset.annotate(
                first_name_dist=Levenshtein(
                    Lower(F("profile__first_name")),
                    first_name,
                ),
            )
            .filter(first_name_dist__lte=5)
            .order_by("first_name_dist")
        )
