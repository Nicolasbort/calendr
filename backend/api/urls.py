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
professional_router = routers.SimpleRouter()
customer_router = routers.SimpleRouter()

router.register("city", CityViewSet, "city")
router.register("profession", ProfessionViewSet, "profession")
router.register("plan", PlanViewSet, "plan")
router.register("test", TestViewSet, "log")
router.register("sign-up", SignUpViewSet, "sign-up")

# Professional routes
professional_router.register(
    "notification",
    Professional.NotificationViewSet,
    "notification",
)
professional_router.register(
    "appointment",
    Professional.AppointmentViewSet,
    "appointment",
)
professional_router.register(
    "calendar",
    Professional.CalendarViewSet,
    "calendar",
)
professional_router.register(
    "patient",
    Professional.PatientViewSet,
    "patient",
)
professional_router.register(
    "oauth",
    Professional.OauthViewSet,
    "oauth",
)

# Professional Calendar routes
calendar_router = routers.NestedSimpleRouter(
    professional_router,
    "calendar",
    lookup="calendar",
)
calendar_router.register(
    "session",
    Professional.SessionViewSet,
    "calendar-session",
)

# Customer routes
customer_router.register(
    "",
    Customer.CustomerViewSet,
    "customer",
)
customer_router.register(
    "appointment",
    Customer.AppointmentViewSet,
    "customer-appointment",
)
customer_router.register(
    "professional",
    Customer.ProfessionalViewSet,
    "customer-professional",
)

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    path("me/", include(professional_router.urls)),
    path("me/", include(calendar_router.urls)),
    path("customer/", include(customer_router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", LoggedUserView.as_view(), name="logged_user"),
    path("swagger/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
]
