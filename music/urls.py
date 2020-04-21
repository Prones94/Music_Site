from django.urls import path
from .views import ArtistListView, AlbumDetailView
from . import views


urlpatterns =[
    path('', ArtistListView.as_view(), name='home'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('album/<int:artist_id>/', views.album_detail, name='album_detail'),
]