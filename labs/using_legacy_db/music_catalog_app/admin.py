from django.contrib import admin
from . import models

admin.site.register(models.Album)
admin.site.register(models.Artist)
admin.site.register(models.Genre)
admin.site.register(models.Track)