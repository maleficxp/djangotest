# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

# Create your models here.

class Artist(models.Model):
    name = models.CharField(verbose_name=u'Имя', max_length=200)
    def __unicode__(self):
        return self.name
 
class Track(models.Model):
    title = models.CharField(verbose_name=u'Название', max_length=200)
    artist = models.ForeignKey(Artist, verbose_name=u'Исполнитель', null=True)
    def __unicode__(self):
        return self.artist.name + ' - ' + self.title
 
class Playlist(models.Model):
    title = models.CharField(verbose_name=u'Название', max_length=200)
    created_time = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)
    tracks = models.ManyToManyField(Track, related_name="present_in_lists")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    
    def __unicode__(self):
        return self.title
    
    def get_tracks_count(self):
        return len(self.tracks.all())
    
    get_tracks_count.short_description = u'Кол-во треков в плейлисте'
    
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('music:playlist', kwargs={'pk':self.pk})

