"""Management command to import songs from the provided data set."""

import csv
import time
from pathlib import Path
from typing import Final

from django.core.management.base import BaseCommand, CommandError, CommandParser

from songs.models import Song


class Command(BaseCommand):
    help = "Imports all songs from the example data set provided."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "csv_file",
            nargs=1,
            type=str,
            help="The location of the CSV file to read from",
        )

    def handle(self, *args, **options) -> None:
        csv_file = Path(options.get("csv_file", [None])[0])
        if not csv_file.exists():
            raise CommandError("CSV file does not exist!")

        with csv_file.open(newline="") as file:
            reader = csv.reader(
                file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            next(reader)
            for row in reader:
                duration = time.strptime(row[6], "%M:%S")
                Song.objects.get_or_create(
                    name=row[0],
                    rank=row[1],
                    album=row[2],
                    writers=row[3],
                    singer=row[4],
                    release_year=row[5],
                    song_time=duration.tm_min * 60 + duration.tm_sec,
                    spotify_streams=row[7].replace(",", ""),
                    rolling_stone_rank=row[8],
                    nme_rank=row[9] or None,
                    ug_views=row[10],
                    ug_favourites=row[11],
                )
