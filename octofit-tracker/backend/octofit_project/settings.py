import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-secret")
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
if os.environ.get("CODESPACE_NAME"):
    ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "octofit_tracker",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "octofit_project.urls"

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "octofit_db",
        "CLIENT": {"host": "mongodb://localhost:27017"},
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

TIME_ZONE = "UTC"
USE_TZ = True

# CORS (dev)
CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

STATIC_URL = '/static/'
