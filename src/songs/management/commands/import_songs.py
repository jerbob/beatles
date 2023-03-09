"""Management command to import songs from the provided data set."""

import csv
import time
from typing import Final

import requests
from django.core.management.base import BaseCommand

from songs.models import Song


DATASET_URL: Final[
    str
] = "https://gist.githubusercontent.com/jerbob/e83483e53148f43dc8de4970edc1c3f1/raw/7243aa2cc96f863499530aa0e80a5a0a1dc659f6/songs.csv"


class Command(BaseCommand):
    help = "Imports all songs from the example data set provided."

    def handle(self, *args, **options) -> None:
        content = requests.get(DATASET_URL, stream=True).iter_lines()
        lines = (line.decode() for line in content)
        csv_lines = csv.reader(
            lines, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        next(csv_lines)
        for row in csv_lines:
            print(row)
            print(row[3])
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
