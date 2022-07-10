import logging
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent





SECRET_KEY = 'django-insecure-lr9rjq1ka7$*ig))jb)_drhp*l-=%sd91dp1wt1&6!7ap*f9g_'


DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1']




INSTALLED_APPS = [
    'grappelli',
    'filebrowser',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'app',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'tinymce',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Русский'),
]

TIME_ZONE = 'Europe/Moscow'


USE_I18N = True

USE_L10N = True

USE_TZ = True




SITE_ID = 1



LOGIN_URL = '/accounts/login/'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'



ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_UNIQUE_USERNAME = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


LOGIN_REDIRECT_URL = '/'

ACCOUNT_FORMS = {'signup': 'project.models.BasicSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'Skill.testing'
EMAIL_HOST_PASSWORD = 'qAzSe$123'
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

DEFAULT_FROM_EMAIL = 'Skill.testing@yandex.ru'
SERVER_EMAIL = 'Skill.testing@yandex.ru'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
        'general': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'errors': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'warning': {
            'format': '%(asctime)s %(pathname)s %(levelname)s %(message)s'
        },

    },

    'handlers': {
        'console': {

            'class': 'logging.StreamHandler',
            'formatter': 'console',

        },

        'general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'general',
            'filename': 'general.log',

        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'errors',
            'filename': 'errors.log'
        },
        'security': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'general',
            'filename': 'security.log'
        },
    },
    'loggers': {
        '': {

            'handlers': ['console'],
            'propagate': True
        },
        'project': {
            'level': 'INFO',
            'handlers': ['general'],
            'propagate': True
         },
        'app': {
            'level': 'INFO',
            'handlers': ['general'],
            'propagate': True
         },
        'django': {
            'level': 'INFO',
            'handlers': ['general'],
            'propagate': True
         },

        'django.template': {
            'level': 'ERROR',
            'handlers': ['errors'],
            'propagate': True
        },
        'django.db_backends': {
            'level': 'ERROR',
            'handlers': ['errors'],
            'propagate': True
        },
        'django.security': {
            'level': 'ERROR',
            'handlers': ['security'],
            'propagate': True
        },
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
PROJECT_DIR = os.path.dirname(__file__)

TINYMCE_SPELLCHECKER = True
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tinymce")

FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''

X_FRAME_OPTIONS = 'SAMEORIGIN'

TINYMCE_DEFAULT_CONFIG = {
    "relative_urls": False,
    "remove_script_host": False,
    "convert_urls": True,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 50,
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',

    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    "language": "ru",
}