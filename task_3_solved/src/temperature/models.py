from django.db import models

from django.conf import settings
from django.db import models
from django.db.models import Q


class Temperature(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


