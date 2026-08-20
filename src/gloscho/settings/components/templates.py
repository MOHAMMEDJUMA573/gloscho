TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            f"{BASE_DIR}/templates/", # type:ignore
            "./templates/", # type:ignore i.e for docker deploy
        ], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.csp",
                "django.template.context_processors.request",
            ],
        },
    },
]
