from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        REDIRECT_MAP = {
            "institution": "schools:school_app_dashboard",
            "instructor": "admin:index",
            "student": "teachers:teacher_app_dashboard",
            "guardian": "account_logout",
            "other": "account_logout"
        }

        return super().get_login_redirect_url(request)