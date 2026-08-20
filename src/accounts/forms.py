# from allauth.account.forms import SignupForm
# from django.core.exceptions import ValidationError
# from better_profanity import profanity
# from django.utils.translation import gettext_lazy as _

# ACCOUNT_USERNAME_BLACKLIST = [
#     "admin", "administrator", "root", "system", "superuser", "sysadmin",
#     "moderator", "mod", "staff", "support", "help", "official", "verified",
#     "security", "billing", "account", "webmaster", "host", "guest",
#     "api", "dev", "developer", "beta", "test", "demo", "null", "none",
#     "undefined", "unknown", "error", "success", "warning", "info",
#     "verify", "confirmation", "password", "login", "signup", "auth",
#     "payment", "credit", "wallet", "bank", "official_account",
#     "spam", "bot", "robot", "advertising", "promo", "free", "gift",
# ]

# BLACKLIST_SET = {w.lower() for w in ACCOUNT_USERNAME_BLACKLIST}

# class ImprovisedSignupForm(SignupForm):
#     def clean_username(self):
#         username = self.cleaned_data.get("username")

#         if username:
#             if profanity.contains_profanity(username):
#                 raise ValidationError(
#                     _(f"The username {profanity.censor(username)} is not allowed!")
#                 )

#             if username.lower() in BLACKLIST_SET:
#                 raise ValidationError(
#                     _(f"The username {username} is not allowed.")
#                 )

#         return username
