from .base import *   #LLAMANDO AL ARCHIVO BASE 

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = ["15.228.201.80"]

import os
#REMPLAZAR DATOS DE LA BASE DE DATOS ACTUAL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'triunfoApi',
        'USER': 'triunfo23',
        'PASSWORD': 'triunfo2023$.',
        'HOST': 'database-triunfo1.ctpv9egj42p9.sa-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/




