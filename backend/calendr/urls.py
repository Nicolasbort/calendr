from django.contrib import admin
from django.urls import include, path

# Not used when using calendr/hosts.py
# Keep it here for maybe future uses
# urlpatterns = [
#     path("api/", include("api.urls")),
#     path("admin/", include("administration.urls")),
# ]

urlpatterns = [
    path("", include("api.urls")),
    path("", include("administration.urls")),
]
