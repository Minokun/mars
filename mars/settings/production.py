from mars.settings.base import *

DB_NAME = 'mars'
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = '1234QWERasdf@'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'HOST': DB_HOST,
        'USER': DB_USER,
        'PASSWORD': DB_PASS
    }
}