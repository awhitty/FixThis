# Django settings for FixThis project.
import os
cwd = os.getcwd()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'HOST': 'ec2-54-243-125-4.compute-1.amazonaws.com',
        'PORT': '5432',
        'NAME': 'ddqenrropkc298',                      # Or path to database file if using sqlite3.
        'USER': 'zuwfisdrensnww',
        'PASSWORD': 'BwCzTLL34wsH5TmReUQMuvwf7I',
    }
}

# def get_cache():
#   import os
#   try:
#     os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHIER_SERVERS']
#     os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME']
#     os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD']
#     return {
#       'default': {
#         'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
#         'LOCATION': os.environ['MEMCACHIER_SERVERS'],
#         'TIMEOUT': 500,
#         'BINARY': True,
#       }
#     }
#   except:
#     return {
#       'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': '127.0.0.1:11211',
#       }
#     }

# CACHES = get_cache()

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# MEDIA_ROOT = cwd + '/media/'

# # URL that handles the media served from MEDIA_ROOT. Make sure to use a
# # trailing slash.
# # Examples: "http://example.com/media/", "http://media.example.com/"
# MEDIA_URL = '/media/'

# # Absolute path to the directory static files should be collected to.
# # Don't put anything in this directory yourself; store your static files
# # in apps' "static/" subdirectories and in STATICFILES_DIRS.
# # Example: "/var/www/example.com/static/"
# STATIC_ROOT = cwd + '/static/'

# # URL prefix for static files.
# # Example: "http://example.com/static/", "http://static.example.com/"
# STATIC_URL = '/static/'

DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = "media"
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = "static"
AWS_ACCESS_KEY_ID = "AKIAIEDYWPP54C3FPF4A"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "fixthis-storage"

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_CACHE_BUSTER = 'Pow'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

THUMBNAIL_ALIASES = {
    '': {
        'small_square': {'size': (50, 50), 'crop': True},
    },
}

AUTH_PROFILE_MODULE = "FixThis.Profile"

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qf6h3d3w@fku1ig+s0ule24^lq#ucgp$=o05a9(cd^$aei$k2q'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

AUTHENTICATION_BACKENDS = (
    'FixThis.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'FixThis.middleware.DisableCSRF',
    # 'FixThis.middleware.EnsureLocation',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages"
)

ROOT_URLCONF = 'FixThis.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'FixThis.wsgi.application'

TEMPLATE_DIRS = (
    cwd + '/templates/'
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS = (
    # Django's contributed apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',

    # Our app:
    'FixThis',

    # Third-party apps
    'south',
    'gunicorn',
    'places',
    # 'sorl.thumbnail',
    'html5',
    'taggit',
    'storages',
    's3_folder_storage',
    # 'debug_toolbar',
    'athumb',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
