from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.account.decorators import verified_email_required
import uuid
from django.utils.translation import gettext_lazy as _


#***--------------------***#***--------------------***
#Dashboard-chief views
#***--------------------***
def dashboard(request):
    return HttpResponse("Welcome bwana chief")
    