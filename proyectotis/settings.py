"""
Django settings for proyectotis project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qe2i-@deobewo9hi%v5af#*re$1s@2ze=t-98-_q3r)#x9pf=m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition


#Aplicaciones utilizadas en el esquema publico de la herramienta / usadas por todos
SHARED_APPS = (
    #APP DE LA HERRAMIENTA DJANGO-TENANTS
    #APP QUE CONTIENE EL MANEJO DE TENANTS
    'productortenant',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'bootstrap3',
)
#aplicaciones privadas
TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.messages',
    'gestionfruta',
)
#Modelos del tenant, son la creación del productor
TENANT_MODEL = "productortenant.Productor"  # app.Model
TENANT_DOMAIN_MODEL = "productortenant.Domain"

INSTALLED_APPS = list(set(SHARED_APPS + TENANT_APPS))



MIDDLEWARE_CLASSES = [
    #Agregar esta clase para el uso de tenants
    'tenant_schemas.middleware.TenantMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
WSGI_APPLICATION = 'proyectotis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'agrofruta',
        #'USER': 'postgres',
        #'PASSWORD': 'postgres',
        #'HOST': '127.0.0.1',
        #'PORT': '5432',
    #}
#}

#Configuración Web Servidor analogo
DATABASES = {
        'default': {

            #'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'ENGINE': 'django_tenants.postgresql_backend',
            'NAME': 'tendencias',
            'USER': 'tendencias',
            'PASSWORD': 'tendencias',
            #'HOST': '172.31.5.162',   #Servidor de base de datos Amazon
            'HOST': 'ec2-52-36-225-236.us-west-2.compute.amazonaws.com',
            'PORT': '5432',                    
        }
    }

#Esto es necesario para que se puedan trabajar tenants
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    #
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/templateProyecto'),],
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


ROOT_URLCONF = 'proyectotis.private_urls'
PUBLIC_SCHEMA_URLCONF = 'proyectotis.public_urls'
PUBLIC_SCHEMA_NAME = 'public'
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#Staticos
STATIC_URL = '/static/'
STATICFILES_DIRS=(BASE_DIR,'static',)
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static_collected')

#Imagenes
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

