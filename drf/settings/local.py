from .base import *   #LLAMANDO AL ARCHIVO BASE 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


#conexion EN LOCAL REMPALZAR DATOS POR NUEVA BASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'triunfoApi',
        'USER': 'postgres',
        'PASSWORD': 'sm26209547',
        'HOST': 'localhost', 
        'PORT': '5433'      
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

