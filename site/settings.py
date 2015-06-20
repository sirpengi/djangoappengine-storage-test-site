from djangoappengine.settings_base import *

import os

DEBUG = True

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '+e$4+da!bt!rqkke)c9e&*wcd)i3c3c1bitl0#cr(hy!%s34@q'

TIME_ZONE = 'US/Hawaii'

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.messages',
	'django.contrib.sessions',
	
	'djangotoolbox',
	'dbindexer',
	'filetransfers',
	
	'macros',
	
	'basesite',
	
	# djangoappengine should come last, so it can override a few manage.py commands
	'djangoappengine',
)

MIDDLEWARE_CLASSES = (
	# This loads the index definitions, so it has to come first
	'autoload.middleware.AutoloadMiddleware',
	
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.request',
	'django.core.context_processors.media',
	'django.contrib.messages.context_processors.messages',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

DEFAULT_FILE_STORAGE = 'basesite.storage.GoogleCloudStorage'
PREPARE_UPLOAD_BACKEND = 'basesite.storage.prepare_upload'

GOOGLE_CLOUD_STORAGE_BUCKET = 'gcs-upload.appspot.com'
