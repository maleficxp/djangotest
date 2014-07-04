# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

from music.models import Track, Artist, Playlist

class TrackMethodTests(TestCase):

    def test_track_to_string(self):
        """
        track string presentation must be equal to artist and title
        """
        artist = Artist(name="Artist Name")
        artist.save()
        track = Track(artist=artist, title="Track Title")
        self.assertEqual(str(track), artist.name + ' - ' + track.title)
        
        
def create_playlist(title, user):
    return Playlist.objects.create(title=title, user=user)

class PlaylistViewTests(TestCase):
    def test_index_view_with_no_playlists(self):
        """
        If no playlists exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('music:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u"Нет ни одного плейлиста.")
        self.assertQuerysetEqual(response.context['playlists'], [])
        
    def test_index_view_with_no_playlists_for_anonymous(self):
        """
        If user not logged, an appropriate message should be displayed.
        """
        User = get_user_model()
        user = User.objects.create_user('test', 'test@test.com', 'test')
        create_playlist(title="Test playlist", user=user)

        response = self.client.get(reverse('music:index'))
        self.assertContains(response, u"Нет ни одного плейлиста.")
        self.assertQuerysetEqual(response.context['playlists'], [])
        
    def test_index_view_with_a_playlist(self):
        """
        Playlist should be displayed on the index page.
        """
        User = get_user_model()
        user = User.objects.create_user('test', 'test@test.com', 'test')
        self.client.login(username='test',password='test')
        
        create_playlist(title="Test playlist", user=user)
        
        response = self.client.get(reverse('music:index'))
        self.assertQuerysetEqual(
            response.context['playlists'],
            ['<Playlist: Test playlist>']
        )