# encoding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.

from music.models import Track, Artist, Playlist

class TrackMethodTests(TestCase):

    def test_track_to_string(self):
        """
        track string presentation must be equal to artist and title
        """
        artist = Artist(name="Artist Name")
        track = Track(artist=artist, title="Track Title")
        self.assertEqual(str(track), artist.name + ' - ' + track.title)
        
        
def create_playlist(title):
    return Playlist.objects.create(title=title)

class PlaylistViewTests(TestCase):
    def test_index_view_with_no_playlists(self):
        """
        If no playlists exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('music:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u"Нет ни одного плейлиста.")
        self.assertQuerysetEqual(response.context['playlists'], [])
        
    def test_index_view_with_a_playlist(self):
        """
        Playlist should be displayed on the index page.
        """
        create_playlist(title=u"Тестовый плейлист")
        response = self.client.get(reverse('music:index'))
        self.assertQuerysetEqual(
            response.context['playlists'],
            [u'<Playlist: Тестовый плейлист>']
        )