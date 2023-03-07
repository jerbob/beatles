"""Base reusable configurations for the application."""

from configurations import Configuration, values

from core import BaseConfigurationMixin


class DummyConfiguration(BaseConfigurationMixin, Configuration):
    """Dummy settings for use during linting, formatting and other ephemeral tasks."""

    ALLOWED_HOSTS = ["*"]

    DEBUG = True
    SECRET_KEY = values.Value("deadbeef")
