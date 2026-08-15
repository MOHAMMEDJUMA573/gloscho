from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_not_required

@login_not_required
def homepage(request):
    if request.user.is_authenticated:
        pass #redirect based on user type
    template = "gloscho/index.html"
    context = {}
    return render(request, template, context)