from django.db import models
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField
from tagging.fields import TagField

class AbstractAccount(models.Model):
    '''
    A base class for social media accounts. These items include profile and
    auth information, and are iterated over by their importer.
    '''
    username = models.CharField(max_length=50)
    network  = models.ForeignKey('SocialNetwork')
    active   = models.BooleanField(default=False, help_text='Should this account be scraped for updates?')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.username or base_url

class AbstractItem(models.Model):
    '''
    A base class for a social media post. This is the main model; each network
    may implement other related models.
    '''
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255)
    remote_url  = models.URLField(verify_exists=False)
    resource_id = models.CharField(max_length=255)
    frozen      = models.BooleanField(default=False, help_text='Exempt this item from updating via importer?')
    created     = models.DateTimeField()
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

class SocialNetwork(models.Model):
    name = models.CharField(max_length=50, help_text='The name of the network')
    url = models.URLField(help_text='The URL of the network, ex http://twitter.com/')
    api_url = models.URLField(blank=True, null=True, verify_exists=False, help_text="The base URL of the API or scrape point, if different; ex: http://api.twitter.com/1/")

    def __unicode__(self):
        return self.name
        
    def resource(self):
        return self.api_url or self.url

class BehanceAccount(AbstractAccount):
    '''
    A Behance account containing auth info and user profile information.
    '''
    name = models.CharField(verbose_name='Display Name', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.name

class BehanceField(models.Model):
    '''
    A field object within the Behance network. This is a professional field,
    not field in the abstract model sense of the word.
    '''
    field      = models.CharField(max_length=50)
    slug       = models.SlugField(max_length=50)
    remote_url = models.URLField(verify_exists=False)

    def __unicode__(self):
        return self.field

class BehanceImage(models.Model):
    '''
    A screenshot belonging to a behance project.
    '''
    image = ImageField(upload_to='uploads/behance')
    item = models.ForeignKey('BehanceItem')

    def __unicode__(self):
        return '[%s] Image for %s' % (self.id, self.item,)

class BehanceItem(AbstractItem):
    '''
    An atomic Behance project.
    '''
    thumbnail = ImageField(upload_to='uploads/behance')
    authors   = models.ManyToManyField('BehanceAccount', null=True, blank=True)
    tags      = TagField(blank=True, null=True, help_text='These are system-wide tags; tag pages are not linked to Behance')
    fields    = models.ManyToManyField('BehanceField', blank=True, null=True)


def ensure_slug(sender, **kwargs):
    instance = kwargs['instance']
    if not instance.slug:
        if hasattr(instance, 'name'):
            instance.slug = slugify(instance.name)
        elif hasattr(instance, 'title'):
            instance.slug = slugify(instance.title)
        elif hasattr(instance, 'tag'):
            instance.slug = slugify(instance.tag)

models.signals.pre_save.connect(ensure_slug, sender=BehanceItem)
models.signals.pre_save.connect(ensure_slug, sender=BehanceField)