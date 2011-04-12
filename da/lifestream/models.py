from django.db import models

class AbstractPost(models.Model):
    title      = models.CharField()
    slug       = models.CharField()
    remote_url = models.URLField()
    created    = models.DateTimeField()
    updated    = models.DateTimeField()

class FlickrPhoto(AbstractPost):
    pass

