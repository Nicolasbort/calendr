from api.models import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "phone",
                    "is_staff",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    list_filter = ("email", "is_staff", "is_superuser", "groups")
    search_fields = ("email", "first_name", "last_name", "email")
    ordering = (
        "-is_staff",
        "email",
    )
