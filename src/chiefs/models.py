from django.db import models
import uuid
from accounts.models import CustomUser

# Create your models here.
# ======================================
# 1. Chief Model
# ======================================
class ChiefProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="chief_profile"
    )
    chief_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )

    def __str__(self):
        return f"{self.chief_id} --- {self.user.email}"