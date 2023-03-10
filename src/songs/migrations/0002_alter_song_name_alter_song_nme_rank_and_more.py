# Generated by Django 4.1.7 on 2023-03-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("songs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Song Name"),
        ),
        migrations.AlterField(
            model_name="song",
            name="nme_rank",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="NME Top 50 Beatles Songs Ranking"
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="release_year",
            field=models.IntegerField(verbose_name="Year Released"),
        ),
        migrations.AlterField(
            model_name="song",
            name="rolling_stone_rank",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Rolling Stone 100 Greatest Beatles Songs Ranking",
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="song_time",
            field=models.DurationField(verbose_name="Song Time"),
        ),
        migrations.AlterField(
            model_name="song",
            name="spotify_streams",
            field=models.IntegerField(default=0, verbose_name="Spotify Streams"),
        ),
        migrations.AlterField(
            model_name="song",
            name="ug_favourites",
            field=models.IntegerField(default=0, verbose_name="UG Favourites"),
        ),
        migrations.AlterField(
            model_name="song",
            name="ug_views",
            field=models.IntegerField(default=0, verbose_name="UG Views"),
        ),
        migrations.AlterField(
            model_name="song",
            name="writers",
            field=models.TextField(
                help_text="For multiple writers, place each on a new line.",
                verbose_name="Song Writer",
            ),
        ),
    ]
