import os
import django


dirname = os.path.dirname
DJANGO_ROOT = dirname(os.path.realpath(django.__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(dirname(__file__),"..",".."))
ENV_ROOT = os.path.dirname(os.path.dirname(PROJECT_ROOT))

# The print name of the desk; appended to things like email subject lines
PROJECT_NAME = 'Made of Awesome'

# The url slug of the desk; appended to things like media_url
PROJECT_SLUG = 'madeofaweso.me'


ADMINS = (
    ('Dan Drinkard', 'dan.drinkard@gmail.com'),
)
MANAGERS = ADMINS
DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
CACHEBUSTER = 'version=%s' % os.environ.get('CACHEBUSTER', 'dev')
ROOT_URLCONF = '%s.urls' % PROJECT_SLUG

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'ckeditor',
    'sorl.thumbnail',
    'form_utils',
    'south',
    'tagging',
    'chronograph',
    '%s.blog' % PROJECT_SLUG,
    '%s.lifestream' % PROJECT_SLUG,
)


# URL CONFIG
# Statics are collected out of apps' /static/ folders via management command;
# This is where they go, not where they're found.
# /data/projects/htdocs/static/%s/' % PROJECT_SLUG
# media10.washingtonpost.com/apps/static/%s/' % PROJECT_SLUG
STATIC_URL = 'http://127.0.0.1/django/static/%s/' % PROJECT_SLUG
STATIC_ROOT = PROJECT_ROOT + '/static/%s/' % PROJECT_SLUG

# Admin uploads will go to MEDIA_ROOT
MEDIA_URL = 'http://127.0.0.1/django/media/%s/' % PROJECT_SLUG
MEDIA_ROOT = PROJECT_ROOT + '/media/%s/' % PROJECT_SLUG

ADMIN_MEDIA_PREFIX = "http://127.0.0.1/django/static/%s/admin/" % PROJECT_SLUG


# EMAIL CONFIG
EMAIL_SUBJECT_PREFIX = "[Django - %s]" % PROJECT_NAME


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'context_processors.cachebuster',
)

## Templates are found in each app's templates/<appname> folder.
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)


CKEDITOR_MEDIA_PREFIX = "%sckeditor/" % MEDIA_URL
CKEDITOR_UPLOAD_PATH = "%suploads/" % MEDIA_ROOT

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'kama',
        'toolbar': 'Custom',
        'height': 300,
        'width': '85%',
        'toolbar_Custom': [
            ['Source','-','Preview',],
            ['Cut','Copy','Paste','PasteText','PasteFromWord'],
            ['SpellChecker','Scayt'],
            ['Undo','Redo'],
            ['Find','Replace'],
            ['SelectAll','RemoveFormat'],
            ['TextColor','BGColor'],
            '/',
            ['Format','-','Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['Link','Unlink','Anchor','Image','Flash','Table','HorizontalRule'],
        ]
    },
}

THUMBNAIL_FORMAT = 'PNG' #safer on mac

from localsettings import *
