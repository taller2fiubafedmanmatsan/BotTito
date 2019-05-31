from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    mute_time = models.DateTimeField('date mute')

