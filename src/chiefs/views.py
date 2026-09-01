from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.account.decorators import verified_email_required
import uuid
from django.utils.translation import gettext_lazy as _
from .models import ChiefProfile


#***--------------------***#***--------------------***
#Dashboard-chief views
#***--------------------***
def dashboard(request):
    try:
        user_chiefsprofile = request.user.chief_profile
    except ChiefProfile.DoesNotExist:
        return HttpResponse("<h2> Such a profile does not exist for the user! </h2>")
    
    return HttpResponse(f"Welcome to your chief's Profile! <h3>{user_chiefsprofile.chief_id}</h3>")
    