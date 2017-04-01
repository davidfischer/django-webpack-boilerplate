"""
Django settings for boilerplate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TESTING = False

# ALLOWED_HOSTS is required in production
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'boilerplate',
)

MIDDLEWARE_CLASSES = (
    # These two should be first
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'boilerplate.urls'

LOGIN_URL = 'login'


# TEMPLATE CONFIGURATION
# See:  https://docs.djangoproject.com/en/1.11/ref/templates/api/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# DATABASES
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# INTERNATIONALIZATION
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# STATIC FILES (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# http://whitenoise.evans.io/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    # Output directory of webpack
    os.path.join(BASE_DIR, 'assets', 'output'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Note: This key only used for development and testing.
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#secret-key
SECRET_KEY = '(ex91e(f0c^pw#)73kdia%mak+5a@_-)0x%40$2)nhvpx6k0@eu4e#'


# CACHING
# Using a local memory cache for development and testing
# and a more hardened cache in production
# See: https://docs.djangoproject.com/en/1.11/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}


# SESSIONS
# See: https://docs.djangoproject.com/en/1.11/topics/http/sessions/
# Using signed cookie sessions. No session data is stored server side,
# but sessions are tamper proof as long as the SECRET_KEY is a secret.
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


# EMAIL CONFIGURATION
# https://docs.djangoproject.com/en/1.11/topics/email/
# In development, emails are not sent and just logged to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SERVER_EMAIL = 'info@boilerplate.com'
DEFAULT_FROM_EMAIL = SERVER_EMAIL
EMAIL_TIMEOUT = 5


# LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See: http://docs.djangoproject.com/en/1.11/topics/logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)-8s %(asctime)s [%(name)s] '
                      '%(module)s.%(funcName)s():%(lineno)d - %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins'],
            'propagate': True,
        },
    }
}
