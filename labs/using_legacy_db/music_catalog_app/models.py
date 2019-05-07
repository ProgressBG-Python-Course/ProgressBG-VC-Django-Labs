# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Artist(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_fav = models.IntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist'

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'genre'

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    is_fav = models.IntegerField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    artist = models.ManyToManyField(Artist)
    genre = models.ManyToManyField(Genre)


    class Meta:
        managed = False
        db_table = 'album'

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    is_fav = models.IntegerField(blank=True, null=True)
    album = models.ForeignKey(Album, models.DO_NOTHING)
    artist = models.ManyToManyField(Artist)

    class Meta:
        managed = False
        db_table = 'track'

    def __str__(self):
        return self.name


