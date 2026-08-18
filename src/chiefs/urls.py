from django.urls import path, include
from . import views

# namespace 
app_name = "chiefs"

# primary urls 
urlpatterns = [
    path("", views.dashboard, name="chief_app_dashboard")
]
