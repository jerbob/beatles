"""Base configuration for the application."""

from pathlib import Path

from configurations import values


class BaseConfigurationMixin:
    """Some default settings that are shared across configurations."""

    ALLOWED_HOSTS = []

    USE_TZ = True
    USE_I18N = True
    USE_L10N = True

    DEBUG = values.BooleanValue(False)
    AUTH_USER_MODEL = values.Value("core.User")
    CACHALOT_EMABLED = values.BooleanValue(True)
    ASGI_APPLICATION = values.Value("core.asgi.application")

    TIME_ZONE = "UTC"
    LANGUAGE_CODE = "en-gb"
    ROOT_URLCONF = "core.urls"

    BASE_DIR = Path(__file__).resolve().parent.parent
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    STATIC_ROOT = values.Value("static")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    LOGIN_URL = "/login/"
    STATIC_URL = "/static/"
    LOGOUT_URL = "/logout/"
    LOGOUT_REDIRECT_URL = "/"

    CACHES = values.CacheURLValue("dummy://")
    DATABASES = values.DatabaseURLValue("sqlite:////tmp/sqlite.db")

    INSTALLED_APPS = values.ListValue(
        [
            "core",
            "songs",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "rest_framework",
        ]
    )

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["core/templates"],
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

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        },
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    ]

    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.BasicAuthentication",
            "rest_framework.authentication.SessionAuthentication",
        ],
    }
