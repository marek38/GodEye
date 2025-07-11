from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from monitoring.models import Camera
from monitoring.management.commands.generate_mediamtx_config import Command

@receiver([post_save, post_delete], sender=Camera)
def regenerate_mediamtx_on_change(sender, **kwargs):
    Command().handle()
