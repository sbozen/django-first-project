from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'isPublished',)
    list_display_links = ('name',)
    list_filter = ('name', 'created_date',)
    list_editable = ('isPublished',)
    search_fields = ('name', 'description',)
    list_per_page = 1


# Register your models here.
admin.site.register(Movie)
