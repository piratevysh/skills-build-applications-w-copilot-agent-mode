import os
from django.urls import path, include
from rest_framework import routers
from . import views


codespace_name = os.environ.get("CODESPACE_NAME")
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

router = routers.DefaultRouter()
router.register(r"users", views.UserProfileViewSet)
router.register(r"teams", views.TeamViewSet)
router.register(r"activities", views.ActivityViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
