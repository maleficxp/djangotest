from django.conf.urls import patterns, url

from music import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /music/playlist/1/
    url(r'^playlist/(?P<pk>\d+)/$', views.PlaylistView.as_view(), name='playlist'),
    url(r'^playlist/add$', views.PlaylistAddView.as_view(), name='playlist_add'),
)
