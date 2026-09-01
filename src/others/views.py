from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.account.decorators import verified_email_required
import uuid
from django.utils.translation import gettext_lazy as _
from .models import OthersProfile


#***--------------------***#***--------------------***
#Dashboard-others views
#***--------------------***
def dashboard(request):
    try:
        user_othersprofile = request.user.others_profile
    except OthersProfile.DoesNotExist:
        return HttpResponse("<h2> Such a profile does not exist for the user! </h2>")
    return HttpResponse(f"Welcome to your Others profile page! <h3>{user_othersprofile.user_id}</h3>")
    