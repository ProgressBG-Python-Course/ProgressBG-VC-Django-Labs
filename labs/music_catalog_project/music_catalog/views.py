from django.shortcuts import render, HttpResponse
from .forms import FormArtist, FormArtist_DjangoForm
from .models import Artist
import pdb


def index(request):
  return render(request, 'music_catalog/index.html', {} )

def artist(request):  
  # form=FormArtist(request.POST,request.FILES or None)

  if request.method == 'GET': 
    form=FormArtist()   
    return render(request, 'music_catalog/artist.html', {'form': form} )
  else:
    form=FormArtist(request.POST,request.FILES)
    # validate data
    if form.is_valid():
      form.save()    
    else:
      print(f"\n--->{form.errors.__repr__()}<---")
      
      # show filled in form with error msg
      return render(request, 'music_catalog/artist.html', {'form': form} )

    return render(request, 'music_catalog/index.html', {} )

def artist_submit(request):
  return render(request, 'music_catalog/artist.html', {} )


def album(request):
  return HttpResponse('album')


def genre(request):
  return HttpResponse('genre')

def track(request):
  return HttpResponse('track')
