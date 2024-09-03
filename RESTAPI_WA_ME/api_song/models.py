from django.db import models

# Create your models here.

class Song(models.Model):
    SONG_NAME = models.CharField(max_length=100)
    SONG_PATH = models.CharField(max_length=100)
    PLAYS = models.IntegerField(default=0)
