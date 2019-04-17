from django.shortcuts import render, HttpResponse
from .forms import FormArtist, FormArtist_DjangoForm
from .models import Artist
import pdb


def index(request):
  return render(request, 'music_catalog/index.html', {} )

def artist(request):  
  artist_form=FormArtist(request.POST or None)

  if request.method == 'GET':
    # artist_form = FormArtist()
    # load empty form for user to fill in
    
    return render(request, 'music_catalog/artist.html', {'form': artist_form} )
  else:
    # artist_form = FormArtist_DjangoForm(request.POST)
    # return HttpResponse(request.POST.get('name'))

    # validate data
    if artist_form.is_valid():
      name = artist_form.cleaned_data['name']
      about = artist_form.cleaned_data['about']
      thumbnail = artist_form.cleaned_data['thumbnail']
      birth_date = artist_form.cleaned_data['birth_date']
      is_fav = artist_form.cleaned_data['is_fav']

      # commit cleaned data to DB          
      record, created = Artist.objects.update_or_create(
        name=name, 
        about=about, 
        birth_date=birth_date, 
        is_fav=is_fav
      )
      print(f"##############created: {created}")
      print(f"\n##############record: {record}")      

    else:
      print(f"\n--->{artist_form.errors.__repr__()}<---")
      # pdb.set_trace()
      
      # show filled in form with error msg

    return HttpResponse(request.POST.get('name'))

def artist_submit(request):
  return render(request, 'music_catalog/artist.html', {} )


def album(request):
  return HttpResponse('album')


def genre(request):
  return HttpResponse('genre')

def track(request):
  return HttpResponse('track')
