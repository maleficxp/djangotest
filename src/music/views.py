from django.views import generic
from music.models import Playlist

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'playlists'
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Playlist.objects.order_by('-created_time').filter(user=self.request.user)
        else:
            return []

class PlaylistView(generic.edit.UpdateView):
    model = Playlist
    template_name = 'music/playlist.html'
    fields = ['title', 'tracks']


class PlaylistAddView(generic.edit.CreateView):
    model = Playlist
    template_name = 'music/playlist.html'
    fields = ['title', 'tracks']
    
    def form_valid(self, form):
        response = super(PlaylistAddView, self).form_valid(form)
        # save playlist owner
        self.object.user = self.request.user 
        self.object.save()
        return response


