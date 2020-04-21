import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    # albums = models.ManyToManyField('Album', on_delete=models.CASCADE)
    # albums = models.ManyToManyField('Album')
    hometown = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Album(models.Model):
    name=models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    released = models.DateField(blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return self.name