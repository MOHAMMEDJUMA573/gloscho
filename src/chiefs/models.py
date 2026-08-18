from django.db import models
import uuid
from accounts.models import CustomUser

#function to generate random chief id
def generate_unique_chief_id():
    while True:
        new_id = f"CHF-{uuid.uuid4().hex[:12].upper()}"
        if not ChiefProfile.objects.filter(chief_id=new_id).exists():
            return new_id
        
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
    chief_id = models.CharField(
        default=generate_unique_chief_id,
        unique=True,
        db_index=True,
        editable=False
    )

    def __str__(self):
        return f"{self.chief_id} --- {self.chief_email}"