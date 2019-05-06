# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    is_fav = models.IntegerField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'


class AlbumArtist(models.Model):
    album = models.ForeignKey(Album, models.DO_NOTHING, primary_key=True)
    artist = models.ForeignKey('Artist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'album_artist'
        unique_together = (('album', 'artist'),)


class AlbumGenre(models.Model):
    album = models.ForeignKey(Album, models.DO_NOTHING, primary_key=True)
    genre = models.ForeignKey('Genre', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'album_genre'
        unique_together = (('album', 'genre'),)


class Artist(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_fav = models.IntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist'


class Genre(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class Track(models.Model):
    name = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    is_fav = models.IntegerField(blank=True, null=True)
    album = models.ForeignKey(Album, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'track'


class TrackArtist(models.Model):
    track = models.ForeignKey(Track, models.DO_NOTHING, primary_key=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'track_artist'
        unique_together = (('track', 'artist'),)
