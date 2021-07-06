from django.contrib import admin
from .models import MovieCollection


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre')


admin.site.register(MovieCollection, MovieAdmin)
