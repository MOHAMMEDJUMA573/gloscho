# Email
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

DEFAULT_FROM_EMAIL = '"gloScho, Inc" <contact@gloscho.com>'

if DEBUG: # type:ignore
    MAILERS = {
        'default': {
            'BACKEND': 'django.core.mail.backends.console.EmailBackend',
        },
    }
else:
    MAILERS = {
        "default": {
            "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
            "OPTIONS": {
                "host": "smtp.gmail.com",
                "use_tls": True,
                "use_ssl": False,
                "port": 587,
                "username": config("APP_EMAIL", default=""), # type:ignore
                "password": config("APP_EMAIL_PASSWORD", default=""), # type:ignore
            },
        },
    }
