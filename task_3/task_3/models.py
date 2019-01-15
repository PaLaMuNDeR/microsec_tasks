from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Temperature(models.Model):
    value = models.FloatField(help_text='Value in Celsius')
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

