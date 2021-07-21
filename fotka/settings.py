import os
import sys
import datetime
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'modeltranslation',
    'grappelli_modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'photo',
    'clients',
    'modeles',
    'home_buh',
    'studio_buh',

    'sorl.thumbnail',
    'django_cleanup',
    'django_user_agents',
    'django_filters',
    'accounts.apps.AccountsConfig',
    'djoser',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'django.contrib.sitemaps',
]

LOGIN_REDIRECT_URL = 'auth/users/me/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'fotka.urls'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=30),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'fotka.wsgi.application'

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

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


def gettext(s): return s


LANGUAGES = [
    ('ru', 'RU'),
    ('uk', 'UA'),
    ('en', 'EN'),
]
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

THUMBNAIL_ALIASES = {
    "": {
        "small": {"size": (150, 150)}
    },
}

try:
    from .local_conf import *
except ImportError:
    from .conf import *
