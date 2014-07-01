from django.conf.urls import patterns, url

from music import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /music/playlist/1/
    url(r'^playlist/(?P<playlist_id>\d+)/$', views.playlist, name='playlist'),
)
