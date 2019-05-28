from django.db import models

# Create your models here.
class Cliente(models.Model):
    cliente_nombre = models.CharField(max_length=200)
    mute_end = models.DateTimeField('date mute')

