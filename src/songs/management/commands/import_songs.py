"""Management command to import songs from the provided data set."""

from django.core.management.base import BaseCommand, CommandError

from songs.models import Song


class Command(BaseCommand):
    help = "Imports all songs from the example data set provided."

    def handle(self, *args, **options) -> None:
        ...
