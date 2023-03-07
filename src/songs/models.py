from django.db import models


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
    singer = models.CharField(max_length=255, blank=False, null=False)
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
        verbose_name="UG Views",
    )
    ug_favourites = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name="UG Favourites",
    )
