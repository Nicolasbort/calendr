from api.views import (
    AppointmentViewSet,
    CityViewSet,
    LoggedUserView,
    PatientViewSet,
    PlanViewSet,
    ProfessionViewSet,
    ProfileViewSet,
    CalendarViewSet,
    SignUpViewSet,
)
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

router.register("profession", ProfessionViewSet, basename="profession")
router.register("plan", PlanViewSet, basename="plan")
router.register("calendar", CalendarViewSet, basename="calendar")
router.register("city", CityViewSet, basename="city")
router.register("profile", ProfileViewSet, basename="profile")
router.register("patient", PatientViewSet, basename="patient")
router.register("appointment", AppointmentViewSet, basename="appointment")
router.register("sign-up", SignUpViewSet, basename="sign_up")

app_name = "api"
urlpatterns = [
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", LoggedUserView.as_view(), name="logged_user"),
] + router.urls
