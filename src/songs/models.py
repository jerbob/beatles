import re
from pathlib import Path
from typing import Optional

from django.conf import settings
from django.db import models
from django.utils.functional import cached_property


class Song(models.Model):
    """Model representing a single beatles song."""

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="Song Name",
    )
    rank = models.IntegerField(blank=False, null=False)
    album = models.CharField(max_length=255, blank=True, null=False, default="")
    writers = models.TextField(
        blank=False,
        null=False,
        verbose_name="Song Writer",
        help_text="For multiple writers, place each on a new line.",
    )
    singer = models.TextField(blank=False, null=False)
    release_year = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Year Released",
    )
    song_time = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Song Time",
        help_text="The duration of the song in seconds.",
    )
    spotify_streams = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name="Spotify Streams",
    )
    rolling_stone_rank = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Rolling Stone Top 100 Rank",
    )
    nme_rank = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="NME Top 50 Rank",
    )
    ug_views = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name="Ultimate Guitar Views",
    )
    ug_favourites = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name="Ultimate Guitar Favourites",
    )

    @cached_property
    def slug(self) -> str:
        """Generate a slug used to find the lyrics for this song."""
        return "-".join(re.sub("[^a-z ]", "", self.name.lower()).split(" "))

    @cached_property
    def lyrics(self) -> Optional[str]:
        """Read the lyrics file for this song and return the contents."""
        file = (settings.BASE_DIR / f"../data/beatles_lyrics/{self.slug}.txt").resolve()
        if file.exists():
            return file.resolve().read_text()
        return None
