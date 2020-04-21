from django.urls import path
from .views import ArtistListView
from . import views


urlpatterns =[
    path('', ArtistListView.as_view(), name='home'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('album/<int:album_id>/album', views.album_detail, name='album_detail'),
    path('song/<int:song_id>/song', views.song_detail, name='song_detail')
]