"""ASGI config for the beatles project."""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "DummyConfiguration")

import configurations

configurations.setup()

from django.core.asgi import get_asgi_application

application = get_asgi_application()
