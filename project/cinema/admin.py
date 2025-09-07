from django.contrib import admin
from .models import Genre, Movie, Comment
# Register your models here.

admin.site.register(Genre)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('text', 'user')


class MovieAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('name', 'release_date', 'genre')

admin.site.register(Movie, MovieAdmin)