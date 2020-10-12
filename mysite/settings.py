import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'meza.meza.alt@gmail.com'
EMAIL_HOST_PASSWORD = 'Xaxteh39'
EMAIL_PORT = 587


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q+t723*9rq*glik^20h7n^sb%xgw#7*95ax!flfg9idfad1s7f'

# SECURITY WARNING: don't run with debug turned on in production!2
DEBUG = False #Para produccion dejar en false y cargara con plantillas de error standart y en local en true pero cargara errores por default
#TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []
DISABLE_COLLECTSTATIC = 1
ALLOWED_HOSTS = ['virtual-code.herokuapp.com', '127.0.0.1']
#        '*',] #para produccion colocar host de heroku y  para local quitar

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'import_export',
    'aplicaciones.base',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.0/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
# # STATICFILES_DIRS = [
# #     os.path.join(BASE_DIR, 'static')
# # ]
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# PROJECT_DIR = os.path.dirname(__file__)
# TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, '../templates'),)


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#FUNCIONAN PARA LOCAL!

STATIC_URL = '/static/'
#STATICFILES_DIRS = (BASE_DIR,'static')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
if DEBUG:
        STATICFILES_DIRS = [(
            os.path.join(BASE_DIR, 'static')
        )]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
PROJECT_DIR = os.path.dirname(__file__)
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, '../templates'),)


#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)