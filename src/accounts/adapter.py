from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse
import uuid
from django.db import transaction
from others.models import OthersProfile

class CustomAccountAdapter(DefaultAccountAdapter):
    def populate_username(self, request, user):
        user.username = uuid.uuid4().hex

        return super().populate_username(request, user)

    @transaction.atomic
    def save_user(self, request, user, form, commit = True):
        user = super().save_user(request, user, form, commit)
        if commit:
            OthersProfile.objects.create(user=user)

        return user
    
    def get_login_redirect_url(self, request):
        REDIRECT_MAP = {
            "chief": "main_app_home",
            "instructor": "account_logout",
            "student": "account_logout",
            "guardian": "account_logout",
            "notide": "others:others_app_dashboard"
        }
        user = request.user
        redirect_url = REDIRECT_MAP.get(user.user_type)
        if redirect_url:
            return reverse(redirect_url)


        return super().get_login_redirect_url(request)