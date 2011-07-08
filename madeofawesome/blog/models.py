from django.db import models
from sorl.thumbnail import ImageField
from tagging.fields import TagField

import datetime

STATUS_CHOICES = (('draft', 'Draft'),
                  ('published', 'Published'),
                  ('scheduled', 'Scheduled'),
                  ('private', 'Private'),
                  )

class Post(models.Model):

    title        = models.CharField(max_length=100)
    slug         = models.SlugField(max_length=100, unique=True)
    content      = models.TextField()
    excerpt      = models.TextField()
    image        = ImageField(blank=True, null=True, upload_to='uploads')
    tags         = TagField()
    status       = models.CharField(max_length=30, choices=STATUS_CHOICES, default='draft')
    created      = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.title
