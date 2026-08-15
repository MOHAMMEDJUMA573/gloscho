
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    f"{BASE_DIR}/staticfilesdev", # type:ignore
]
STATIC_ROOT=f"{BASE_DIR}/staticfiles"  # type:ignore

