from django.contrib import admin

# Register your models here.

from music.models import Artist, Track, Playlist

class TrackInline(admin.TabularInline):
    model = Playlist.tracks.through
 
class PlaylistAdmin(admin.ModelAdmin):
    inlines = [TrackInline]
    exclude = ('tracks',)
    list_display = ('title', 'created_time', 'get_tracks_count')
    list_filter = ['created_time']
    search_fields = ['title']

admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Playlist, PlaylistAdmin)
