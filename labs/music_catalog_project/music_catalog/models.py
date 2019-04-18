from django.db import models

# Create your models here.
from django.db import models

''' 
  Genre will list the information about tracks
'''
class Genre(models.Model):
  name = models.CharField('Name', max_length=50, help_text='Name of the Track')
  notes = models.TextField('About', null=True, blank=True, help_text='Notes')

  class Meta:      
    ordering = ['name']
  def __str__(self):
    return self.name


''' 
  Artist will contain information about the artist
'''
class Artist(models.Model):
    name = models.CharField('Name', max_length=50, help_text='Enter the name of the Artist')
    about = models.TextField('About', null=True, blank=True, help_text='About Artist')
    thumbnail = models.ImageField("Image", help_text='Uplaod Image of the Artist', upload_to='static/artist/images', default='static/artist/default.jpg')
    birth_date = models.DateField('Birth Date', null=True, blank=True, help_text='Birth date of Artist')
    is_fav = models.BooleanField('Favourite', help_text='Tick if favourite', default= False)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    
''' 
  Album will store info about albums
'''
class Album(models.Model):
    name = models.CharField('Name', max_length=50, help_text='Enter the name of the Album')
    date = models.DateTimeField(null=True, blank=True)
    about = models.TextField('Description', null=True, blank=True, help_text='About Album')
    thumbnail = models.ImageField("Image", help_text='Upload Image of the Artist', upload_to='static/album/images', default='static/album/default.jpg')
    is_fav = models.BooleanField('Favourite', help_text='Tick if favourite', default= False)
    release_date = models.DateField("Release Year", null=True, blank=True, help_text='Release date of Album')    
    genre = models.ManyToManyField(Genre)        
    artist = models.ManyToManyField(Artist)        
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


''' 
  Track will list the information about tracks
'''
class Track(models.Model):
  name = models.CharField('Name', max_length=50, help_text='Name of the Track')
  duration = models.DurationField(null=True, blank=True)
  lyrics = models.TextField('Lyrics', null=True, blank=True, help_text='Track lyrics')  
  is_fav = models.BooleanField('Favourite', help_text='Tick if favourite', default= False)
  # language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
  album = models.ForeignKey(Album,on_delete=models.PROTECT)  
  # TODO: when artist is NULL, set track.artist to Album.artist with custom methods without custom Manaer
  artist = models.ManyToManyField('Artist', related_name ='track_artist')

  class Meta:      
      ordering = ['name']


  def __str__(self):
      return self.name




