AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_FORMS = {
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'confirm_login_code': 'allauth.account.forms.ConfirmLoginCodeForm',
    'login': 'allauth.account.forms.LoginForm',
    'request_login_code': 'allauth.account.forms.RequestLoginCodeForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'signup': 'allauth.account.forms.SignupForm',
    'user_token': 'allauth.account.forms.UserTokenForm',
}

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
ACCOUNT_CHANGE_EMAIL=True
ACCOUNT_PRESERVE_USERNAME_CASING=False
ACCOUNT_USERNAME_MIN_LENGTH=4

USERSESSIONS_TRACK_ACTIVITY=True



ALLAUTH_UI_THEME = "emerald"
