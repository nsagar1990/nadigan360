#Django settings for nadigan360 project.
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Niranjan Sagar', 'bnsagar90@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE'	: 'django.db.backends.mysql', 
        'NAME'		: 'NADIGAN',                   
        'USER'		: 'root',
        'PASSWORD'	: 'sagar',
        'HOST'		: '',                      
        'PORT'		: '',                    
    }
}

ALLOWED_HOSTS 	= []
TIME_ZONE 	= 'America/Chicago' #remember to change this
LANGUAGE_CODE 	= 'en-us'
SITE_ID 	= 1
USE_I18N 	= True
USE_L10N 	= True
USE_TZ 		= True


MEDIA_ROOT = ''
MEDIA_URL = ''


"**** Static files related configs ********"
STATIC_ROOT = '/var/www/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'templates', 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
"******************************************"



SECRET_KEY = 'b-_zp^eemolo9&odo@!6bvj#_=1iu#6wr*v*h)9e@#!6s4@n=('

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nadigan360.urls'

WSGI_APPLICATION = 'nadigan360.wsgi.application'

TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, 'templates'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nd360',
    #'south',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
