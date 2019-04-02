from django.shortcuts import render, HttpResponse
from .forms import FormArtist



def index(request):
  return render(request, 'music_catalog/index.html', {} )

def artist(request):
  if request.method == 'GET':
    # load empty form for user to fill in
    artist_form = FormArtist()
    return render(request, 'music_catalog/artist.html', {'form': artist_form} )
  else:
    return HttpResponse(request.POST['artist_name'])
    #   PASSWORD: ''
    # validate data
    # if is_valid:
    #   # commit user data to DB
    # else:
    #   # show filled in form with error msg

def artist_submit(request):
  return render(request, 'music_catalog/artist.html', {} )


def album(request):
  return HttpResponse('album')


def genre(request):
  return HttpResponse('genre')

def track(request):
  return HttpResponse('track')
