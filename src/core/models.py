"""Database models used across the application."""

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom AUTH_USER representing a logged in user."""
