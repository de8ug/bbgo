# -*- coding: utf-8 -*-
"""
Django settings for bbgo project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from collections import namedtuple
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Theme
THEME = 'haru'
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
THEME_DIR = os.path.join(BASE_DIR, 'templates', THEME)

# Localization
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if 'DJANGO_DEBUG' in os.environ:
    if os.environ['DJANGO_DEBUG'] == 'Debug':
        DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_PARTY_APPS = (
    'rosetta',
    'jsi18ncache',
)
EDITOR_APPS = (
    'django_summernote',
)
LOCAL_APPS = (
    'accounts',
    'msgs',
    'core',
    'blogs',
    'boards',
    'spams',
    'teams',
    'vaults',
    'recipes',
    'aliases',
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + EDITOR_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bbgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(THEME_DIR),
            os.path.join(TEMPLATES_DIR),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'bbgo.wsgi.application'

# Secrets
# Load sensitive data from secrets.json
try:
    with open(os.path.join(BASE_DIR, "secrets.json")) as f:
        data = json.loads(f.read())
    SecretsNamedTuple = \
        namedtuple('SecretsNamedTuple', data.keys(), verbose=False)
    secrets = SecretsNamedTuple(*[data[x] for x in data.keys()])
    SECRET_KEY = getattr(secrets, "SECRET_KEY")
    DB_NAME = getattr(secrets, "DB_NAME")
    DB_USER = getattr(secrets, "DB_USER")
    DB_PASSWORD = getattr(secrets, "DB_PASSWORD")
    EMAIL_HOST = getattr(secrets, "EMAIL_HOST")
    EMAIL_HOST_USER = getattr(secrets, "EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = getattr(secrets, "EMAIL_HOST_PASSWORD")
    DEFAUL_FROM_EMAIL = getattr(secrets, "DEFAUL_FROM_EMAIL")
    SERVER_EMAIL = getattr(secrets, "SERVER_EMAIL")
    SITE_NAME = getattr(secrets, "SITE_NAME")
    SITE_LOGO = getattr(secrets, "SITE_LOGO")
    SITE_INFO = getattr(secrets, "SITE_INFO")
    ADMIN_EMAIL = getattr(secrets, "ADMIN_EMAIL")
    BLOG_CATEGORY = getattr(secrets, "BLOG_CATEGORY")
    AKISMET_API_KEY = getattr(secrets, "AKISMET_API_KEY")
    BLOG_URL = getattr(secrets, "BLOG_URL")
    SENSE_UP_CLIENT = getattr(secrets, "SENSE_UP_CLIENT")
    SENSE_UP_SLOT = getattr(secrets, "SENSE_UP_SLOT")
    SENSE_DOWN_CLIENT = getattr(secrets, "SENSE_DOWN_CLIENT")
    SENSE_DOWN_SLOT = getattr(secrets, "SENSE_DOWN_SLOT")
    SENSE_SIDE_CLIENT = getattr(secrets, "SENSE_SIDE_CLIENT")
    SENSE_SIDE_SLOT = getattr(secrets, "SENSE_SIDE_SLOT")
    FB_APP_ID = getattr(secrets, "FB_APP_ID")
except IOError:
    SECRET_KEY = 'k8n13h0y@$=v$uxg*^brlv9$#hm8w7nye6km!shc*&bkgkcd*p'
    DB_NAME = ''
    DB_USER = ''
    DB_PASSWORD = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAUL_FROM_EMAIL = ''
    SERVER_EMAIL = ''
    SITE_NAME = ''
    SITE_LOGO = ''
    SITE_INFO = ''
    ADMIN_EMAIL = ''
    BLOG_CATEGORY = ''
    AKISMET_API_KEY = ''
    BLOG_URL = ''
    SENSE_UP_CLIENT = ''
    SENSE_UP_SLOT = ''
    SENSE_DOWN_CLIENT = ''
    SENSE_DOWN_SLOT = ''
    SENSE_SIDE_CLIENT = ''
    SENSE_SIDE_SLOT = ''
    FB_APP_ID = ''
f.close()

try:
    with open(os.path.join(BASE_DIR, "VERSION")) as f:
        APP_VERSION = f.readline()
except IOError:
    APP_VERSION = 0.1
f.close()

EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

# SSL
if not DEBUG:
    SESSION_COOKIE_SECURE = True,
    SECURE_SSL_REDIRECT = True,
    CSRF_COOKIE_SECURE = True,


# Summernote customization
if DEBUG:
    SUMMERNOTE_CONFIG = {
        'lang': 'ko-KR',
        'width': '100%',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'strikethrough']],
            ['super', ['superscript', 'subscript']],
            ['fontname', ['fontname', 'fontsize', 'color', 'clear']],
            ['para', ['height', 'paragraph']],
            ['format', ['ul', 'hr', 'table']],
            ['insert', ['link', 'picture', 'video']],
            ['misc', ['codeview']],
        ],
        'attachment_filesize_limit': 2 * 1024 * 1024,
        'base_css': (
            '/static/css/bootstrap.min.css',
        ),
        'base_js': (
            '/static/js/thirdparty/jquery-3.2.1.min.js',
            '/static/js/thirdparty/bootstrap.min.js',
        ),
    }
else:
    SUMMERNOTE_CONFIG = {
        'lang': 'ko-KR',
        'width': '100%',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'strikethrough']],
            ['super', ['superscript', 'subscript']],
            ['fontname', ['fontname', 'fontsize', 'color', 'clear']],
            ['para', ['height', 'paragraph']],
            ['format', ['ul', 'hr', 'table']],
            ['insert', ['link', 'picture', 'video']],
            ['misc', ['codeview']],
        ],
        'attachment_filesize_limit': 2 * 1024 * 1024,
    }


# Setting for Member
ID_MIN_LENGTH = 4
ID_MAX_LENGTH = 16  # Maximum 30
NICKNAME_MIN_LENGTH = 2
NICKNAME_MAX_LENGTH = 10
ENABLE_NICKNAME = True
VERIFICATION_CODE_VALID = 24 * 3600  # 24 hours
PORTRAIT_SIZE_LIMIT = 500 * 1024
POINT_ARTICLE = 5  # point per article
POINT_REPLY = 1  # point per reply

# Setting for Alarm
ENABLE_ALARM_POLLING = True
DEFAULT_ALARM_INTERVAL = 30  # 30 secs
ALARM_INBOX_MAX = 100
MIN_ALARM_INTERVAL = 30  # 30 sec
MAX_ALARM_INTERVAL = 3600  # 1 hour

# Setting for Bookmark
MAX_BOOKMARKS = 10

# Setting for Msg
MSG_TEXT_MAX = 1000
MSG_LIST_COUNT = 10
OLD_MSG_THRESHOLD = 100  # days

# Setting for Board
HOT_THRESHOLD = 10  # emphasize like, dislike count if gte

# Setting for Reply
REPLY_TEXT_MAX = 2000
REPLY_IMAGE_AVAILABLE = True
REPLY_IMAGE_SIZE_LIMIT = 1 * 1024 * 1024
REPLY_AUTO_RENEW_MS = 30 * 1000

# Setting for Blog
ENABLE_MEMBER_BLOG = True
ENABLE_ANONYMOUS_COMMENT = True
COMMENT_TEXT_MAX = 2000
USERNAME_MAX = 23
BLOG_LIST_COUNT = 10
DASHBOARD_LIST_COUNT = 50
DASHBOARD_POST_COUNT = 10
DASHBOARD_COMMENT_COUNT = 5
DASHBOARD_ARTICLE_COUNT = 20
DASHBOARD_REPLY_COUNT = 10
ENABLE_AKISMET = True

# Use AdSense
ENABLE_ADSENSE = True

# highlight with coding style for <pre> using highlight.js
ENABLE_CODE_HIGHLIGHT = True

# highlight keyword using mark.js
ENABLE_MARK_KEYWORD = True

# Setting for Vault
ENABLE_MASTERKEY = True
MASTERKEY_LENGTH = 6
MASTERKEY_SESSION_TIME = 15  # minutes

# Setting for Recipe
RECIPE_CATEGORY_MAX = 16
RECIPE_NAME_MAX = 32
