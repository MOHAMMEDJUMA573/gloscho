"""
URL configuration for gloscho project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin-gloscho/', admin.site.urls),
    #project urls
    path("", views.homepage, name="main_app_home"),
    #apps urls
    #3rd party urls
]
