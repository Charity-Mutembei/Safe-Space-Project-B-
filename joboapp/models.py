from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255000)

class Message(models.Model):
    value = models.CharField(max_length=255000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=2550000)
    room = models.CharField(max_length=255000000)