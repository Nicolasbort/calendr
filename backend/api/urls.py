from api.views import (
    CityViewSet,
    LoggedUserView,
    PlanViewSet,
    ProfessionViewSet,
    SignUpViewSet,
    TestViewSet,
)
from api.views import customer as Customer
from api.views import professional as Professional
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()

# Read only viewsets
router.register("city", CityViewSet, basename="city")
router.register("profession", ProfessionViewSet, basename="profession")
router.register("plan", PlanViewSet, basename="plan")

router.register("test", TestViewSet, basename="log")
router.register("sign-up", SignUpViewSet, basename="sign-up")
router.register("appointment", Professional.AppointmentViewSet, basename="appointment")
router.register("calendar", Professional.CalendarViewSet, basename="calendar")
router.register("patient", Professional.PatientViewSet, basename="patient")
router.register("oauth", Professional.OauthViewSet, basename="oauth")

# Customer routes
customer_router = routers.SimpleRouter()
customer_router.register("", Customer.CustomerViewSet, basename="customer")
customer_router.register(
    "appointment", Customer.AppointmentViewSet, basename="customer-appointment"
)
customer_router.register(
    "professional", Customer.ProfessionalViewSet, basename="customer-professional"
)

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    path("customer/", include(customer_router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", LoggedUserView.as_view(), name="logged_user"),
    path("swagger/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
]
