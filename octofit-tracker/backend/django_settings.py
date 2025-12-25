import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-secret")
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
if os.environ.get("CODESPACE_NAME"):
    ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "rest_framework",
    "octofit_tracker",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "octofit_tracker.urls"

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
