"""
Django settings for c03_basdat project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Add this line
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add this line
PRODUCTION = os.environ.get('DATABASE_URL') is not None

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l7jb=bda2inky24m-i&g@4_bha0#8p^aii_k!43dl7)stmk_1_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not PRODUCTION

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME', '')

# ALLOWED_HOSTS = [f'{HEROKU_APP_NAME}.herokuapp.com']
ALLOWED_HOSTS = ['*']

if not PRODUCTION:
    ALLOWED_HOSTS += ['.localhost', '127.0.0.1', '[::1]']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

     # Add fitur
    'registrasiPengguna',
    'kategori_apparel',
    'koleksi',
    'koleksi_tokoh',
    'registrasiPengguna'

    'pekerjaan'
    'menggunakan_barang'
    'bekerja',
    'makan',
    'makanan',
    'misi',
    'menjalankan_misi_utama',
    'level',
]

# hapus aja
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'basdat_c03.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # beda
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        ##
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

WSGI_APPLICATION = 'basdat_c03.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# Jangan lupa di uncomment kalo perlu
DATABASE_URL= 'postgres://mpafwjjbldwevd:50c84eb8d286171d50b58f4cede89b2dbb48d94721ba0595bc427a54676abb6f@ec2-54-165-90-230.compute-1.amazonaws.com:5432/d707lr0gagd7tk'
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': dj_database_url.config()
}

if PRODUCTION:
    DATABASES['default'] = dj_database_url.config()

DATABASES['default']=dj_database_url.config()
DATABASES['default']=dj_database_url.config(default=DATABASE_URL)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = 'static/'
# beda
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# for directory in [*STATICFILES_DIRS, STATIC_ROOT]:
#     directory.mkdir(exist_ok=True)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
# Kalo error kita hapus ini
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
