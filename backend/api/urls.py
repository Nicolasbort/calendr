from api.views import SignUpViewSet, TestViewSet
from api.views import customer as Customer
from api.views import professional as Professional
from api.views.logged_user import LoggedUserView
from api.views.plan import PlanViewSet
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
professional_router = routers.SimpleRouter()
customer_router = routers.SimpleRouter()

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
professional_router.register(
    "session",
    Professional.SessionViewSet,
    "session",
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
    path("professional/", include(professional_router.urls)),
    path("customer/", include(customer_router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("whoami/", LoggedUserView.as_view(), name="logged_user"),
    path("swagger/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
]
