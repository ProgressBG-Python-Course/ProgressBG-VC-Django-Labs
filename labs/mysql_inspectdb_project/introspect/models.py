# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MusicCatalogAlbum(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=100)
    is_fav = models.IntegerField()
    release_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'music_catalog_album'



class MusicCatalogArtist(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_fav = models.IntegerField()
    thumbnail = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'music_catalog_artist'



class MusicCatalogAlbumArtist(models.Model):
    album = models.ForeignKey(MusicCatalogAlbum, models.DO_NOTHING)
    artist = models.ForeignKey('MusicCatalogArtist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'music_catalog_album_artist'
        unique_together = (('album', 'artist'),)


class MusicCatalogAlbumGenre(models.Model):
    album = models.ForeignKey(MusicCatalogAlbum, models.DO_NOTHING)
    genre = models.ForeignKey('MusicCatalogGenre', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'music_catalog_album_genre'
        unique_together = (('album', 'genre'),)


class MusicCatalogGenre(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'music_catalog_genre'


class MusicCatalogTrack(models.Model):
    name = models.CharField(max_length=50)
    duration = models.BigIntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    is_fav = models.IntegerField()
    album = models.ForeignKey(MusicCatalogAlbum, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'music_catalog_track'


class MusicCatalogTrackArtist(models.Model):
    track = models.ForeignKey(MusicCatalogTrack, models.DO_NOTHING)
    artist = models.ForeignKey(MusicCatalogArtist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'music_catalog_track_artist'
        unique_together = (('track', 'artist'),)
