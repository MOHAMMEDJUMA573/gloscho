from django.db import models
from chiefs.models import ChiefProfile
import uuid
from pathlib import Path

#function to generate a path
def image_file_upload_handler(instance, filename):
    fname = uuid.uuid4().hex
    ext = Path(filename).suffix
    return f"scprf/{fname}{ext}"

# Create your models here.
# ======================================
# 1. Institution Model
# ======================================
class InstitutionProfile(models.Model):
    owner = models.ForeignKey(
        ChiefProfile,
        on_delete=models.CASCADE,
        related_name="institution_profiles"
    )
    inst_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )
    inst_name = models.CharField(
        max_length=35,
        help_text="institution name."
    )
    # inst_badge = models.ImageField(
    #     upload_to=image_file_upload_handler,
    #     blank=True,
    #     null=True
    # )
    STATUS_CHOICES = [
        ('P', 'Pending 🛞'),
        ('V', 'Verified ✅'),
        ('S', 'Suspended 🚟')
    ]
    inst_status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P',
        help_text="status on the platform e.g Verified"
    )
    inst_creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text="Creation date/time stamp",
        editable=False
    )
    inst_updated_date = models.DateTimeField(
        auto_now=True,
        help_text="Last Modification timestamp"
    )

    def __str__(self):
        return f"{self.inst_name} --- {self.owner.email}"