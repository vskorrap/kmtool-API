import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'k6n4xh!cmjddul61nqub6-16#q8h=h=*3v6*@van$d=om%g6we'

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'GOImplement.GeneralDiscussion',
    'GOImplement.GRM',
    'GOImplement.file_app',
    'corsheaders',
    'django_elasticsearch_dsl',
    'rest_framework',
    'rest_framework.authtoken'
]
# CORS_ORIGIN_WHITELIST = (
#     'google.com',
#     'hostname.example.com',
#     'localhost:8000',
#     '127.0.0.1:9000',
#     'localhost:4200'
# )
# CORS_ALLOW_HEADERS = (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# )
MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
# DEFAULT_PARSER_CLASSES =[
#     'rest_framework.parsers.JSONParser',
#     'rest_framework.parsers.MultiPartParser',
#     'rest_framework.parsers.FileUploadParser',
# ]

ROOT_URLCONF = 'GOImplementAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'GOImplementAPI.wsgi.application'

MEDIA_URL = '/GOImplement/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "GOImplement/media")
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'http://localhost:9200'#'http://131.163.160.58:9200'
    },
}




DATABASES = {
    'default': {
        'NAME': 'KMToolsData',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'hexagon3269.database.windows.net',
        'USER': 'SaiDeepu',
        'PASSWORD': 'PheonixBlaze@1304',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },

    }
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR,'static')
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
)
CORS_ORIGIN_REGEX_WHITELIST = (
    'localhost:4200',
)
