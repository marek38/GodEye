from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Camera
from .utils import generate_mediamtx_config

@receiver([post_save, post_delete], sender=Camera)
def regenerate_mediamtx_on_change(sender, **kwargs):
    generate_mediamtx_config()
