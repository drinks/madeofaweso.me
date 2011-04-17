# Make this unique, and don't share it with anybody.
SECRET_KEY = '8r+eT]pPSVmbr`Kor0[hse=X_17)oII))VKDY*lDv]I7}$Yj43'

# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/Users/drinkarddp/Sites/django-media/moa/'
    
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://localhost/django-media/moa/'

CKEDITOR_MEDIA_PREFIX = "%sckeditor/" % MEDIA_URL
CKEDITOR_UPLOAD_PATH = "%suploads/" % MEDIA_ROOT

