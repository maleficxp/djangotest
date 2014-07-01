# encoding: utf-8

from django.db import models


# Create your models here.

class Artist(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    def __str__(self):
        return self.name
 
class Track(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    artist = models.ForeignKey(Artist, verbose_name='Исполнитель')
    def __str__(self):
        return self.artist.name + ' - ' + self.title
 
class Playlist(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    tracks = models.ManyToManyField(Track, related_name="present_in_lists")
    
    def __str__(self):
        return self.title
    
    def get_tracks_count(self):
        return len(self.tracks.all())
    
    get_tracks_count.short_description = 'Кол-во треков в плейлисте'
    
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('music:playlist', kwargs={'pk':self.pk})
