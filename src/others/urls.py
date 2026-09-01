from django.urls import path, include
from . import views

# namespace 
app_name = "others"

# primary urls 
urlpatterns = [
    path("", views.dashboard, name="others_app_dashboard")
]
