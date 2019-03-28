from django.urls import path
from music import views


# http://127.0.0.1:8000/music/
urlpatterns = [
    path('artists', views.artists, name='artists'),
    # http://127.0.0.1:8000/music/artist_add
    path('artist_add', views.artist_add, name='artist_add'),
]
