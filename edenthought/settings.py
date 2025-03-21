# - Import and initialise our environment variables 

import environ

env = environ.Env()

environ.Env.read_env()


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECRET_KEY = 'django-insecure-h!t094o@bu4cv4m^h8-^ndv(*d0%&#n5d8zlkje@7im(up@%9@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['django-app-u8k9.onrender.com','*']

CSRF_TRUSTED_ORIGINS = ['https://django-app-u8k9.onrender.com']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "onepiece",
    "crispy_forms",
    "crispy_bootstrap5", 
    "storages",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "edenthought.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "edenthought.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
'''

# RDS / PostgreSQL database configuration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        # 'NAME': 'demo_1a',
        # 'USER': 'alex_db2',
        # 'PASSWORD': 'onepiece',
        # 'HOST': 'database-1.czs6eysesorg.ca-central-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


#SMTP Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = 'True'
 
EMAIL_HOST_USER = env('EMAIL_HOST_USER') #GMAIL email address
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') # App Password tdev qcyo gwaq zttc

# EMAIL_HOST_USER = 'alexchristiantbay@gmail.com'
# EMAIL_HOST_PASSWORD = 'tdev qcyo gwaq zttc'
# DEFAULT_FROM_EMAIL = 'alexchristiantbay@gmail.com'
 
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL') # GMAIL email address 


# Amazon S3 Configuration

 # - Enter your AWS access key ID here 
 # - Enter your AWS secret access key here 
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME') # - Enter your AWS bucket name here

# AWS_STORAGE_BUCKET_NAME = 'edenthought-bkt-ca-1'

# storage configuration for S3
STORAGES = {

    # media file (image) management 
    "default": {
        "BACKEND" : "storages.backends.s3boto3.S3StaticStorage",
    },

    # CSS and JS file management 
    "staticfiles": {
        "BACKEND" : "storages.backends.s3boto3.S3StaticStorage",
    },

}

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_FILE_OVERWRITE = False

