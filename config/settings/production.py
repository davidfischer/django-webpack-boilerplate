import os

import dj_database_url

from .common import *  # noqa


# Production Settings
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
def environ(envvar, default=None):
    """
    Load certain sensitive settings from environment variables
    """
    if envvar in os.environ:
        return os.environ[envvar]
    elif default is not None:
        return default
    else:
        raise AttributeError(envvar)


#
# DEBUG must always be False in production
# It is much faster, more stable and more secure
DEBUG = False

#
# Production Secret Key
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#secret-key
SECRET_KEY = environ('DJANGO_SECRET_KEY')

#
# ALLOWED_HOSTS is required in production
ALLOWED_HOSTS = [
    'localhost',
    'djangowebpackboilerplate.herokuapp.com',
]


#
# SESSIONS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

#
# TEMPLATE CONFIGURATION
# See:  https://docs.djangoproject.com/en/1.11/ref/templates/api/#django.template.loaders.cached.Loader
# Cached templates can speed up rendering considerably
TEMPLATES[0]['APP_DIRS'] = False
TEMPLATES[0]['OPTIONS']['loaders'] = [
    (
        'django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]
    ),
]

#
# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.11/topics/db/optimization/
DATABASES['default'] = dj_database_url.config('DATABASE_URL')
DATABASES['default']['ATOMIC_REQUESTS'] = True    # Each request is in a transaction
DATABASES['default']['CONN_MAX_AGE'] = 60 * 10    # 10 minute persistent connections

#
# CACHING
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '{0}/{1}'.format(environ('REDIS_URL', default='redis://127.0.0.1:6379'), 0),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,  # mimics memcache behavior.
                                        # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
        }
    }
}

#
# SECURITY SETTINGS
# See: https://docs.djangoproject.com/en/1.11/ref/middleware/#django.middleware.security.SecurityMiddleware
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365 * 10

#
# EMAIL CONFIGURATION
# https://anymail.readthedocs.io
# EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'  # v3 API
# ANYMAIL = {
#     'SENDGRID_API_KEY': environ('SENDGRID_API_KEY'),
# }
