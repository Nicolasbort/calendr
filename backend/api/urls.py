from api.views import (
    CityViewSet,
    LoggedUserView,
    PlanViewSet,
    ProfessionViewSet,
    ProfileViewSet,
    SignUpViewSet,
    TestViewSet,
)
from api.views.patient import PatientAppointmentViewSet, PatientCalendarViewSet
from api.views.professional import (
    ProfessionalAppointmentViewSet,
    ProfessionalCalendarViewSet,
    ProfessionalPatientViewSet,
    ProfessionalSlotViewSet,
)
from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()

router.register("test", TestViewSet, basename="log")
router.register("profile", ProfileViewSet, basename="profile")
router.register("sign-up", SignUpViewSet, basename="sign-up")
router.register("appointment", ProfessionalAppointmentViewSet, basename="appointment")
router.register("calendar", ProfessionalCalendarViewSet, basename="calendar")
router.register("patient", ProfessionalPatientViewSet, basename="patient")

calendar_router = routers.NestedSimpleRouter(router, "calendar", lookup="calendar")
calendar_router.register("slot", ProfessionalSlotViewSet, basename="calendar-slot")

# Read only viewsets
router.register("city", CityViewSet, basename="city")
router.register("profession", ProfessionViewSet, basename="profession")
router.register("plan", PlanViewSet, basename="plan")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    path("", include(calendar_router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", LoggedUserView.as_view(), name="logged_user"),
]
