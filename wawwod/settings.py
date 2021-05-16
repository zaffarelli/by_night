import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'y-he7pukz&#$z_9c_*r7st6p6cm+tu$i9&h*gbw+z!%p4paw3!'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'collector.apps.CollectorConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'django_yarnpkg',
    'django_node_assets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
    'django_yarnpkg.finders.NodeModulesFinder',
    'django_node_assets.finders.NodeModulesFinder',
)

NODE_MODULES_ROOT = os.path.join(BASE_DIR, 'node_modules')

NODE_PACKAGE_JSON = os.path.join(BASE_DIR, 'package.json')

ROOT_URLCONF = 'wawwod.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'collector/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'collector.context_processors.commons',
            ],
        },
    },
]

LOGPATH = os.path.join(BASE_DIR, 'logs/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(message)s",
            'datefmt': "%d:%H%M%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGPATH + "wawwod.log",
            'maxBytes': 1000000000,
            'backupCount': 3,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console','logfile'],
            'propagate': False,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['console','logfile'],
            'level': 'INFO',
            'propagate': False,
        },
        'collector': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}
WSGI_APPLICATION = 'wawwod.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wawwod',
        # 'NAME': 'redfoxinc',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = 'wawwod_static/'
MEDIA_ROOT = 'wawwod_media/'

# PROJECT_DIR = os.path.dirname(__file__)
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

YARN_INSTALLED_APPS = (
    'chartjs',
    'd3@3.5.5',
    'jquery',
    'jspdf@2.3.1',
    'lodash',
    'svg2pdf',
    'dom-to-image',
    'save-svg-as-png',
)