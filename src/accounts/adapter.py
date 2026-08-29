from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse
import uuid

class CustomAccountAdapter(DefaultAccountAdapter):
    def populate_username(self, request, user):
        user.username = uuid.uuid4().hex

        return super().populate_username(request, user)
    
    def get_login_redirect_url(self, request):
        REDIRECT_MAP = {
            "chief": "/",
            "instructor": "account_logout",
            "student": "account_logout",
            "guardian": "account_logout",
            "other": "/"
        }
        user = request.user
        redirect_url = REDIRECT_MAP.get(user.user_type)
        if redirect_url:
            return reverse(redirect_url)


        return super().get_login_redirect_url(request)