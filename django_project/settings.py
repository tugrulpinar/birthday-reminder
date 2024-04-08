import os
from pathlib import Path
import socket

import environ
from celery.schedules import crontab
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))


SECRET_KEY = env.str("SECRET_KEY", default=get_random_secret_key())

DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS")


INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party
    "allauth",
    "allauth.account",
    "crispy_forms",
    # "crispy_bootstrap5",
    "debug_toolbar",
    "bootstrap_datepicker_plus",
    "bootstrap4",
    "django_htmx",
    'django_celery_results',
    # Local
    "accounts",
    "pages",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # WhiteNoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.middleware.common.CommonMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # Django Debug Toolbar
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",  # django-allauth
]

# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "django_project.urls"

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "django_project.wsgi.application"

# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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


DATABASES = {
    "default": env.db()
}

CONN_MAX_AGE = None
CONN_HEALTH_CHECKS = True

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
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

# https://docs.djangoproject.com/en/dev/topics/i18n/
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"

# https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = "EST"

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-USE_I18N
USE_I18N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# https://whitenoise.readthedocs.io/en/latest/django.html
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}


if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True


# django-crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = env.str("DJANGO_DEFAULT_FROM_EMAIL")
SERVER_EMAIL = env.str("DJANGO_SERVER_EMAIL")
EMAIL_HOST = env.str("DJANGO_EMAIL_HOST")
EMAIL_PORT = env.str("DJANGO_EMAIL_PORT")
EMAIL_HOST_USER = env.str("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("DJANGO_EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
SMTP_DEV = env.bool("SMTP_DEV", False)
ADMIN_EMAIL = env.str("ADMIN_EMAIL", "")

if DEBUG:
    EMAIL_USE_TLS = False

if DEBUG and not SMTP_DEV:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "accounts.CustomUser"

# django-allauth config
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "profile"

# https://django-allauth.readthedocs.io/en/latest/views.html#logout-account-logout
ACCOUNT_LOGOUT_REDIRECT_URL = "landing-page"

# https://django-allauth.readthedocs.io/en/latest/installation.html?highlight=backends
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True


CELERY_BROKER_URL = env.str("REDIS_URL")
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_RESULT_EXTENDED = True


CELERY_BEAT_SCHEDULE = {
    "notify_customers": {
        "task": "pages.tasks.notify_customers",
        "schedule": 5,  # Run daily at 6AM
    },
}


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
