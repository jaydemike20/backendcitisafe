"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9+r035xi96ogx!b=qx7sag9d#hr@5wq!ec&x-t5_^a&t_1u+*y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# # connected to the postgreSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
#     # "default": {
#     # "ENGINE": "django.db.backends.postgresql",
#     # "NAME": "backendcitisafe",
#     # "USER": "postgres",
#     # "PASSWORD": "@Jayde15",
#     # "HOST": "localhost",  # Change this if your PostgreSQL server is on a different host
#     # "PORT": "8080", 
#     # },
    
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jaydemike$citisafeapp',  # Replace with your actual database name
        'USER': 'jaydemike',
        'PASSWORD': '@engracia123',  # Set the MySQL password you've chosen
        'HOST': 'jaydemike.mysql.pythonanywhere-services.com',
        'PORT': '3306',  # MySQL default port
    }
}


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


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True


# mailtrap config
# EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
# EMAIL_HOST_USER = '061df45eb6ebea'
# EMAIL_HOST_PASSWORD = '98494b8a33eec4'
# EMAIL_PORT = '2525'

# GMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True  
EMAIL_HOST_USER = 'jaydemike21@gmail.com'
EMAIL_HOST_PASSWORD = 'epvcwqrbtxtzpgcp'


# frond end
FRONTEND_URL = 'http://localhost:3000'

DEFAULT_FROM_EMAIL = 'jaydemike21@gmail.com'
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
    'DEFAULT_FROM_EMAIL': 'jaydemike21@gmail.com', 
}


AUTH_USER_MODEL = "accounts.User"



#  CELERY SETTINGS
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
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