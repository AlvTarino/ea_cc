from .base import *  # noqa
from .base import BASE_DIR, DATABASES, MIDDLEWARE, INSTALLED_APPS
import os

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '::1']

# Development-specific apps
INSTALLED_APPS += [
    'debug_toolbar',
]

# Development middleware
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
    ]

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Celery
CELERY_TASK_ALWAYS_EAGER = True  # Run tasks synchronously in development

# Database
DATABASES['default']['TEST'] = {
    'NAME': 'test_eastafricom_db',
    'CHARSET': 'utf8',
    'COLLATION': 'utf8_general_ci',
    }

# Static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
