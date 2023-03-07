"""URL configuration for the beatles project."""

from django.urls import path, include


urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("songs/", include("songs.urls")),
]
