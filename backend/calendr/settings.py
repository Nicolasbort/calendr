"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
ENV = os.environ.get("ENV", default="dev").lower()
DEBUG = bool(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = [
    "calendr",
    "api.calendr",
    "management.calendr",
    "localhost",
]

ADMINS = [("Nicolas", "bortoluzzinicolas@gmail.com")]

# Application definition

INSTALLED_APPS = [
    "management",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "django_filters",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "api",
    "django_hosts",
]

MIDDLEWARE = [
    "django_hosts.middleware.HostsRequestMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_hosts.middleware.HostsResponseMiddleware",
]

ROOT_HOSTCONF = "calendr.hosts"
DEFAULT_HOST = "api"
ROOT_URLCONF = "calendr.urls"

# Admin configuration
LOGIN_REDIRECT_URL = "/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Rest Framework settings
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 15,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "username",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
}

SPECTACULAR_SETTINGS = {"TITLE": "Calendr API"}

# Database
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE", "calendr"),
        "USER": os.environ.get("SQL_USER", "calendr"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "calendr_db"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
        "ATOMIC_REQUESTS": True,
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

AUTH_USER_MODEL = "api.Profile"
AUTHENTICATION_BACKENDS = ["api.backends.authentication.CustomAuthBackend"]

# Celery variables
CELERY_BROKER_URL = os.environ.get("REDIS_URL")
CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE

# Logging
LOGGING_FORMATTERS = {
    "verbose": {
        "format": '[{levelname}]: {asctime} - {module} - Logger: {name} - File "{pathname}", line {lineno}: {message}',
        "style": "{",
    },
    "simple": {
        "format": "[{levelname}]: {message}",
        "style": "{",
    },
}

LOGGING_HANDLERS = {
    "console_handler": {
        "class": "logging.StreamHandler",
        "level": "INFO",
        "formatter": "simple",
    },
    "warning_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": f"{BASE_DIR}/logs/application.logs",
        "mode": "a",
        "formatter": "verbose",
        "level": "WARNING",
        "backupCount": 5,
        "maxBytes": 1024 * 1024 * 10,  # 10 MB
    },
    "error_handler": {
        "level": "ERROR",
        "class": "django.utils.log.AdminEmailHandler",
        "include_html": True,
    },
}

LOGGING_LOGGERS = {
    "django": {
        "handlers": ["console_handler", "warning_handler", "error_handler"],
        "level": "INFO",
        "propagate": True,
    },
    "django.request": {
        "handlers": ["warning_handler"],
        "level": "WARNING",
    },
    "django.server": {
        "handlers": ["warning_handler"],
        "level": "INFO",
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": LOGGING_FORMATTERS,
    "handlers": LOGGING_HANDLERS,
    "loggers": LOGGING_LOGGERS,
}

# Email
EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", "false").lower() == "true"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SEND_EMAIL_ACTIVE = os.environ.get("SEND_EMAIL_ACTIVE", "false").lower() == "true"


# Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL"),
    }
}


# OTP
OTP_PERIOD = os.environ.get("OTP_PERIOD")
OTP_SECRET = os.environ.get("OTP_SECRET")

# Google Calendar
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL")
GOOGLE_OAUTH_URL = os.environ.get("GOOGLE_OAUTH_URL")
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.environ.get("GOOGLE_REDIRECT_URI")
