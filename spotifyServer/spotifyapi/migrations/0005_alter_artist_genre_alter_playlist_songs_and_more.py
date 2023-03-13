# Generated by Django 4.1.4 on 2023-03-13 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifyapi', '0004_alter_artist_genre_alter_playlist_songs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, to='spotifyapi.genre'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, null=True, to='spotifyapi.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(blank=True, null=True, to='spotifyapi.artist'),
        ),
    ]
