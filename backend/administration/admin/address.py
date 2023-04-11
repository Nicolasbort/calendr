from api.models import Address
from django.contrib import admin


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "street",
        "number",
        "district",
        "complement",
        "city",
    )
