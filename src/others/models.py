from django.db import models
from accounts.models import CustomUser
import uuid

# Create your models here.
# ======================================
# 1. Others Model
# ======================================
class OthersProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="others_profile"
    )
    others_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )

    def __str__(self):
        return f"{self.others_id} --- {self.user.email}"