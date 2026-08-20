"""
URL configuration for gloscho project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.contrib import admin
from allauth.account.decorators import secure_admin_login
from django.urls import path, include
from . import views

#preventing admin bruteforce
admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

urlpatterns = [
    path('admin-gloscho/', admin.site.urls),
    #project urls
    path("", views.homepage, name="main_app_home"),
    #apps urls
    path("chief/", include("chiefs.urls")),
    #3rd party urls
    path("accounts/", include("allauth.urls")),
]
