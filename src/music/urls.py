from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from music import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /music/playlist/1/
    url(r'^playlist/(?P<pk>\d+)/$', login_required(views.PlaylistView.as_view()), name='playlist'),
    url(r'^playlist/add$', login_required(views.PlaylistAddView.as_view()), name='playlist_add'),
)
