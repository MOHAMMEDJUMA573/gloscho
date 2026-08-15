# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

CONN_MAX_AGE = config("CONN_MAX_AGE", cast=int, default=30) # type:ignore
CONN_HEALTH_CHECKS=True,
DATABASE_URL = config("DATABASE_URL",cast=str, default="") # type:ignore
if DATABASE_URL is not None:
    import dj_database_url
    if not DEBUG:               # type:ignore
        DATABASES = {
            "default": dj_database_url.config(
                default=DATABASE_URL,
                conn_max_age=30,
                conn_health_checks=True,
            )
        }
    elif DEBUG:                 # type:ignore
        LOCAL_DATABASE_PASSWORD = config("LOCAL_DATABASE_PASSWORD",cast=str, default=None) # type:ignore
        LOCAL_DATABASE_USER = config("LOCAL_DATABASE_USER",cast=str, default=None) # type:ignore
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'gloscho',
                'USER': LOCAL_DATABASE_USER,
                'PASSWORD': LOCAL_DATABASE_PASSWORD,
                'HOST': 'localhost',
                'PORT': '',
            }
        }
