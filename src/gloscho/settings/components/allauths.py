AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SIGNUP_FIELDS=['email*', 'password1*', 'password2*']
ACCOUNT_SIGNUP_FORM_HONEYPOT_FIELD="address"
ACCOUNT_LOGIN_METHODS={"email","username"}
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION=True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE=True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1
ACCOUNT_EMAIL_VERIFICATION="mandatory"
LOGIN_REDIRECT_URL="/"
ACCOUNT_SIGNUP_REDIRECT_URL="/"
ACCOUNT_EMAIL_NOTIFICATIONS=True
# ACCOUNT_CHANGE_EMAIL=True
ACCOUNT_MAX_EMAIL_ADDRESSES=2
ACCOUNT_PRESERVE_USERNAME_CASING=False
ACCOUNT_USERNAME_MIN_LENGTH=4
USERSESSIONS_TRACK_ACTIVITY=True

ACCOUNT_ADAPTER = "accounts.adapter.CustomAccountAdapter"



ALLAUTH_UI_THEME = "emerald"
