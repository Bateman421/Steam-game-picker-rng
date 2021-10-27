from django.db import models

# Create your models here.


class GameRng(models.Model):
    id_game = models.CharField(max_length=30)
    name = models.TextField()
    img = models.TextField()
