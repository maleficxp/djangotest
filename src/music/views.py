from django.views import generic

from music.models import Playlist


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'playlists'
    def get_queryset(self):
        return Playlist.objects.order_by('-created_time')

class PlaylistView(generic.edit.UpdateView):
    model = Playlist
    template_name = 'music/playlist.html'

class PlaylistAddView(generic.edit.CreateView):
    model = Playlist
    template_name = 'music/playlist.html'
