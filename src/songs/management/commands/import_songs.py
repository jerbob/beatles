"""Management command to import songs from the provided data set."""

import csv
import time
from pathlib import Path

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
            reader = csv.DictReader(
                file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            for row in reader:
                duration = time.strptime(row["Song Time"], "%M:%S")
                Song.objects.get_or_create(
                    name=row["Song Name"],
                    rank=row["Rank"],
                    album=row["Album"],
                    writers=row["Song Writer"],
                    singer=row["Singer"],
                    release_year=row["Year Released"],
                    song_time=duration.tm_min * 60 + duration.tm_sec,
                    spotify_streams=row["Spotify Streams"].replace(",", ""),
                    rolling_stone_rank=row[
                        "Rolling Stone 100 Greatest Beatles Songs Ranking"
                    ],
                    nme_rank=row["NME Top 50 Beatles Songs Ranking"] or None,
                    ug_views=row["UG Views"],
                    ug_favourites=row["UG Favourites"],
                )
