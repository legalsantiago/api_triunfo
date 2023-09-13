from .base import *   #LLAMANDO AL ARCHIVO BASE 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["15.229.6.215"]

import os
#REMPLAZAR DATOS DE LA BASE DE DATOS ACTUAL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'apiTest',
        'USER': 'triunfo',
        'PASSWORD': 'triunfo2023',
        'HOST': 'databaseaws2.ctpv9egj42p9.sa-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'


