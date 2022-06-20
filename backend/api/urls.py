from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from api.views import (
    ProfessionViewSet,
    PlanViewSet,
    ProfileViewSet,
    PatientViewSet,
    AppointmentViewSet,
    SignUpViewSet,
    LoggedUserView,
)

router = DefaultRouter()

router.register("profession", ProfessionViewSet, basename="profession")
router.register("plan", PlanViewSet, basename="plan")
router.register("profile", ProfileViewSet, basename="profile")
router.register("patient", PatientViewSet, basename="patient")
router.register("appointment", AppointmentViewSet, basename="appointment")
router.register("sign-up", SignUpViewSet, basename="sign_up")

app_name = "api"
urlpatterns = [
    path("token-auth/", obtain_jwt_token),
    path("logged-user/", LoggedUserView.as_view(), name="logged_user"),
] + router.urls
