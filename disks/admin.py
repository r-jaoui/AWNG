from django.contrib import admin
from .models import Album, Artist, Track


# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Artist',)
    list_filter = ('Title', 'Artist',)
    ordering = ('Title', 'Artist')
    search_fields = ('Title', 'Artist')


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    list_filter = ('Name',)
    ordering = ('Name',)
    search_fields = ('Name',)


class TrackAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Album', 'Milliseconds', 'UnitPrice', 'Composer', 'Bytes')
    list_filter = ('Name', 'Album', 'Milliseconds', 'UnitPrice', 'Composer', 'Bytes')
    ordering = ('Name', 'Album')
    search_fields = ('Name', 'Album', 'Composer')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Track, TrackAdmin)