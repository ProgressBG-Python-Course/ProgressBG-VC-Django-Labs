from django.shortcuts import render
from music.models import Artist

# Create your views here.
def index(request):
  artists = Artist.objects.all()
  return render(request, 'music/index.html',{'artists':artists})


def artist_add(request):
  # INSERT into Artist(name="The Cure", notes="alabala")

  Artist.objects.create(name="The Cure", notes="alabala")
  return render(request, 'music/index.html',{})
