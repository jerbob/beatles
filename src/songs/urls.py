"""URL configuration for the songs app."""

from django.urls import path, include

from rest_framework import routers

from songs import views


router = routers.DefaultRouter()
router.register("", views.SongViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
