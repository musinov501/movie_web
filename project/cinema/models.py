from enum import unique
from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=155, unique = True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    release_date = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=500, verbose_name="Matni")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Maqola")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Avtor')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yozilgan vaqti")

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ['-created']