"""Settings that need to be set in order to run the tests."""
import os

DEBUG = True

SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = 'cmsplugin_pdf.tests.urls'

PROJECT_ROOT = os.path.realpath(
    os.path.join(os.path.dirname(__file__), "../"))

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../media/')
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../static/')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'tests/test_static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../templates'),
)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), 'coverage')

COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
    'cms$', '__init__',
]

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_nose',
    'mptt',
    'sekizai',
    'cms.plugins.text',
    'filer',
    'easy_thumbnails',
    'wand',
    'menus',
]

# the following apps are added separatly, because they cause problems with the
# regex lookup for the coverage module excludes.
NON_COVERAGE_APPS = [
    'cms',
]

INTERNAL_APPS = [
    'cmsplugin_pdf',
]

INSTALLED_APPS = EXTERNAL_APPS + NON_COVERAGE_APPS + INTERNAL_APPS

COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS

LANGUAGES = [
    ('en', 'English'),
]

LANGUAGE_CODE = 'en'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

# django-cms settings
CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
)

# easy_thumbnails settings
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

SECRET_KEY = 'NOT A REAL SECRET KEY'
