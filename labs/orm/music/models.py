from django.db import models
from django.utils import timezone

# Create your models here.
class Artist(models.Model):
  name = models.CharField(max_length=45)
  notes = models.TextField(max_length=1000)

  def __str__(self):
    return self.name

class Genre(models.Model):
  name = models.CharField(max_length=50)
  notes = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']
    # db_table = 'GENRE'


class Album(models.Model):
  name = models.CharField(max_length=45)
  notes = models.TextField(max_length=1000)
  release_date = models.DateField(default=timezone.now )
  picture_url=models.URLField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE)
  genre = models.ManyToManyField(Genre)

  def __str__(self):
    return self.name




# class Track(models.Model):
# class Genre(models.Model):