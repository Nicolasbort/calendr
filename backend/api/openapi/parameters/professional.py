from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter

MULTIPLE_LOOKUP_VIEWSET = [
    OpenApiParameter(
        name="multiple_lookup_field",
        type=OpenApiTypes.STR,
        location=OpenApiParameter.PATH,
        description="UUID or username of the professional.",
    )
]
