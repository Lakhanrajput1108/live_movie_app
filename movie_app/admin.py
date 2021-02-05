from django.contrib import admin
from movie_app.models import MovieInfo
# Register your models here.

class MovieDetails(admin.ModelAdmin):
    list_display=['Movie','Release_Year','Actor']
admin.site.register(MovieInfo,MovieDetails)
