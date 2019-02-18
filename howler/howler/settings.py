"""
Django settings for howler project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_^(0#f!ko0m6!by14p!z834m^zg$h-*f98sft(mk6-!(bz)v&('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '10.0.10.180','']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobower',
    'wally_search',
    'settings',
    'doc',
]

# Middleware-order matters!
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Locale: https://docs.djangoproject.com/en/1.10/topics/i18n/translation/#how-django-discovers-language-preference
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'howler.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'howler.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'database',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

TIME_ZONE = 'Asia/Tokyo'  # JST, was before UTC

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "public/static")

STATIC_URL = "/static/"  # How static files are accessed by URL

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "wally_search", "static"),
]

BOWER_INSTALLED_APPS = (
    'jquery',
    'bootstrap',
    'bootstrap-confirmation2',
    'eonasdan-bootstrap-datetimepicker#latest',
    'datatables.net',
    'datatables.net-bs#^1.10.13',
    'showdown#^1.5.1',
)

LANGUAGE_CODE = 'en'  # Default language

LANGUAGES = [
    ('en', 'English'),
    ('ja', '日本語'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

# --- CUSTOM SETTINGS ELASTICSEARCH and SERACH ---
ES_HOSTS = ['10.0.10.180']
ES_DEFAULT_PORT = 9200
ES_TIMEOUT = 30
ES_MAXSIZE_CON = 25
ES_SUPPORTED_INDEX_PREFIX = {'email': 'mailing-{0}',
                             'irc': 'irclogs{0}'}
ES_SUPPORTED_TYPE_NAMES = {'email': 'email',
                           'irc': 'log'}
ES_DATETIME_FORMAT_MAIL = '%Y-%m-%dT%H:%M:%S%z'  # yyyy-MM-dd'T'HH:mm:ssZZ
ES_DATETIME_FORMAT_IRC = '%Y-%m-%dT%H:%M:%S%z'  # yyyy-MM-dd'T'HH:mm:ssZZ
ES_CONFIG_ROOT = '/etc/elasticsearch'

SUPPORTED_LANG_CODES_ANALYZERS = {'ja': 'kuromoji',
                                  'en': 'english',
                                  'un': 'standard'}
FALLBACK_LANG_CODE = 'un'
JA_USER_DICT = 'userdict_ja.txt'  # /etc/elasticsearch/userdict_ja.txt
