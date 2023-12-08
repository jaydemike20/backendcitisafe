"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv  # Python dotenv
import os

load_dotenv()  # loads the configs from .env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9+r035xi96ogx!b=qx7sag9d#hr@5wq!ec&x-t5_^a&t_1u+*y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "daphne",
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
    "accounts",
    "drivers",
    "vehicles",
    "corsheaders",
    "ticket",

]

ASGI_APPLICATION = "config.asgi.application"


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",    
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6380)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# connected to the postgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'citisafeapp',  # Replace with your actual database name
#         'USER': 'root',
#         'PASSWORD': 'admin',  # Set the MySQL password you've chosen
#         'HOST': 'localhost',
#         'PORT': '3306',  # MySQL default port
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
# TIME_ZONE = 'Asia/Manila'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True


# Email credentials
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
EMAIL_USE_TLS = False

if (DEBUG == True):
    EMAIL_HOST = str(os.getenv('DEV_EMAIL_HOST'))
    EMAIL_HOST_USER = str(os.getenv('DEV_EMAIL_HOST_USER'))
    EMAIL_HOST_PASSWORD = str(os.getenv('DEV_EMAIL_HOST_PASSWORD'))
    EMAIL_PORT = str(os.getenv('DEV_EMAIL_PORT'))
else:
    EMAIL_HOST = str(os.getenv('PROD_EMAIL_HOST'))
    EMAIL_HOST_USER = str(os.getenv('PROD_EMAIL_HOST_USER'))
    EMAIL_HOST_PASSWORD = str(os.getenv('PROD_EMAIL_HOST_PASSWORD'))
    EMAIL_PORT = str(os.getenv('PROD_EMAIL_PORT'))
    EMAIL_USE_TLS = str(os.getenv('PROD_EMAIL_TLS'))

# frond end
FRONTEND_URL = 'https://sprincessgenevieve.github.io/citisafeweb/#'

DEFAULT_FROM_EMAIL = 'eTCMFBukidnon@gmail.com'
# my djoser
DJOSER = {
    "SEND_CONFIRMATION_EMAIL": True,
    'LOGIN_FIELD': 'username',
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    "PASSWORD_RESET_CONFIRM_URL": 'reset_password/{uid}/{token}',
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.CustomUserCreateSerializer',
        'user': 'accounts.serializers.CustomUserSerializer',
        'current_user': 'accounts.serializers.CustomUserSerializer',
    },
    'EMAIL' : {
        'confirmation': 'accounts.email.ConfirmationEmail',
        'password_reset': 'accounts.email.CustomPasswordResetEmail',
        'password_changed_confirmation': 'accounts.email.PasswordChangedConfirmationEmail'        
    },    
    'DEFAULT_FROM_EMAIL': 'eTCMFBukidnon@gmail.com', 
}


AUTH_USER_MODEL = "accounts.User"



#  CELERY SETTINGS
CELERY_BROKER_URL = 'redis://127.0.0.1:6380'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6380'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Manila'
CELERY_TASK_ALWAYS_EAGER = True  


from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'update_ticket_status_every_minute': {
        'task': 'ticket.tasks.update_ticket_status',
        'schedule': crontab(minute='*/1'),
    },
}

CSRF_TRUSTED_ORIGINS = ["https://etcmf.keannu1.duckdns.org"]
