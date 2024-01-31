from django.db import models
from django.contrib.auth.models import User

class Source(models.Model):
    url = models.URLField()

class DiscoverThread(models.Model):
    title = models.TextField()
    description = models.TextField()
    views = models.IntegerField()
    branches = models.IntegerField()
    datetime = models.DateTimeField()
    image_url = models.URLField()
    sources = models.ManyToManyField(Source)