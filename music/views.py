from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Artist, Album, Song

# Create your views here.
# def home(request):
#     context ={
#         'artists': Artist.objects.all()
#     }
#     return render(request, 'home.html', context)

class ArtistListView(ListView):
    model = Artist
    template_name= 'home.html'
    context_object_name = 'artists'
    

def artist_detail(request, artist_id):
    albums = Album.objects.filter(artist__id=artist_id)
    artist = Artist.objects.get(id=artist_id)
    
    context = {
        'albums': albums,
        'artist': artist
    }
    return render(request, 'artist_detail.html', context)

def album_detail(request, album_id):
    albums = Album.objects.get(id=album_id)
    songs = Song.objects.filter(album=album_id)
    # albums = Album.objects.filter(artist__name='artist_name')

    context = {
        'albums': albums, 
        'songs': songs
    }
    return render(request, 'album_detail.html',context)

def song_detail(request, song_id):
    songs = Song.objects.get(id=song_id)

    context = {
        'song' : songs
    }
    return render(request, 'song_detail.html', context)