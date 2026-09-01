from django.db import models
from accounts.models import CustomUser

# Create your models here.
class OthersProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="others_profile"
    )
