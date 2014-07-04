from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.utils.translation import ugettext_lazy as _

# Register your models here.

from music.models import Artist, Track, Playlist
from accounts.models import MyUser

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

class MyUserAdmin(UserAdmin):
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth','is_staff')
    

admin.site.register(MyUser, MyUserAdmin)
