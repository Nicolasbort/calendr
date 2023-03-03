from api.views import (
    AppointmentViewSet,
    CalendarViewSet,
    CityViewSet,
    LoggedUserView,
    LogViewSet,
    PatientViewSet,
    PeriodViewSet,
    PlanViewSet,
    ProfessionViewSet,
    ProfileViewSet,
    SignUpViewSet,
)
from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()

router.register("log", LogViewSet, basename="log")

router.register("profession", ProfessionViewSet, basename="profession")
router.register("plan", PlanViewSet, basename="plan")
router.register("calendar", CalendarViewSet, basename="calendar")
router.register("city", CityViewSet, basename="city")
router.register("profile", ProfileViewSet, basename="profile")
router.register("patient", PatientViewSet, basename="patient")
router.register("appointment", AppointmentViewSet, basename="appointment")
router.register("sign-up", SignUpViewSet, basename="sign_up")

calendar_router = routers.NestedSimpleRouter(router, "calendar", lookup="calendar")
calendar_router.register(r"period", PeriodViewSet, basename="calendar-period")

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("", include(calendar_router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", LoggedUserView.as_view(), name="logged_user"),
]
