"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
Default environment is `developement`.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from split_settings.tools import optional, include
from decouple import config

ENV = config('DJANGO_ENV', cast=str, default="production")

base_settings = [
    'components/common.py',
    'components/admins.py',
    'components/docker.py',
    'components/logging.py',
    'components/templates.py',
    'components/database.py',
    'components/rq.py',
    'components/staticf.py',
    'components/emails.py',
    'components/timez.py',
    optional('environments/{0}.py'.format(ENV)),
]

# Include settings:
include(*base_settings)