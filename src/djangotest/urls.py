from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^music/', include('music.urls', namespace='music')),
    url(r'^admin/', include(admin.site.urls))    
)

urlpatterns += staticfiles_urlpatterns()