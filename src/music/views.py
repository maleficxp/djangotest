from django.http import Http404
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from music.models import Playlist

def index(request):
    playlists = Playlist.objects.order_by('-created_time')
    context = {'playlists': playlists}
    return render(request, 'music/index.html', context)

def playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    return render(request, 'music/playlist.html', {'playlist': playlist})

