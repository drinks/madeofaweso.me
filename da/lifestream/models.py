from django.db import models
from django.template.defaultfilters import slugify
from tagging.fields import TagField

class AbstractAuth(models.Model):
    base_url = models.URLField()
    username = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.username or base_url

class AbstractItem(models.Model):
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255)
    remote_url  = models.URLField()
    resource_id = models.CharField(max_length=255)
    created     = models.DateTimeField()
    updated     = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.title
    
class BehanceAuth(AbstractAuth):
    pass

class BehanceAuthor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    remote_url = models.URLField()
    
    def __unicode__(self):
        return self.name

class BehanceItem(AbstractItem):
    thumbnail = models.URLField()
    authors = models.ManyToManyField('BehanceAuthor')
    tags = TagField()
    behance_tags = models.ManyToManyField('BehanceTag', blank=True, null=True)

class BehanceTag(models.Model):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    remote_url = models.URLField()
    
    def __unicode__(self):
        return self.tag


def ensure_slug(sender, **kwargs):
    instance = kwargs['instance']
    if not instance.slug:
        if hasattr(instance, 'name'):
            instance.slug = slugify(instance.name)
        elif hasattr(instance, 'title'):
            instance.slug = slugify(instance.title)
        elif hasattr(instance, 'tag'):
            instance.slug = slugify(instance.tag)

models.signals.pre_save.connect(ensure_slug, sender=BehanceAuthor)
models.signals.pre_save.connect(ensure_slug, sender=BehanceItem)
models.signals.pre_save.connect(ensure_slug, sender=BehanceTag)