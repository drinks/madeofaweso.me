import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

ADMINS = (
    ('Dan Drinkard', 'dan.drinkard@gmail.com'),
)

MANAGERS = ADMINS

PROJECT_ROOT = os.path.dirname(__file__)
ENV_ROOT = os.path.dirname(os.path.dirname(PROJECT_ROOT))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(ENV_ROOT, 'db', 'moa.sqlite3'),
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'moa.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/'.join([PROJECT_ROOT, 'templates']),
    '/'.join([PROJECT_ROOT, 'blog', 'templates']),
    '/'.join([PROJECT_ROOT, 'contact', 'templates']),
    '/'.join([PROJECT_ROOT, 'lifestream', 'templates']),
)

# TEMPLATE_CONTEXT_PROCESSORS = ()

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
    'moa.blog',
    'moa.lifestream',
)

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

from moa.localsettings import *