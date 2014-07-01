from django.contrib import admin

# Register your models here.

from music.models import Artist, Track, Playlist

class TrackInline(admin.StackedInline):
    model = Playlist.tracks.through
 
class PlaylistAdmin(admin.ModelAdmin):
    inlines = [TrackInline]
    exclude = ('tracks',)

admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Playlist, PlaylistAdmin)
