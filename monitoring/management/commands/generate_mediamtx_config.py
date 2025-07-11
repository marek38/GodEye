from django.core.management.base import BaseCommand
from monitoring.models import Camera
import yaml

class Command(BaseCommand):
    help = 'Generates mediamtx.yml from current Camera entries'

    def handle(self, *args, **kwargs):
        config = {
            'paths': {}
        }

        for cam in Camera.objects.all():
            config['paths'][cam.name] = {
                'source': f'rtsp://{cam.username}:{cam.password}@{cam.host}:{cam.port}{cam.stream_path}',
                'sourceOnDemand': True
            }

        with open('mediamtx.yml', 'w') as f:
            yaml.dump(config, f)

        self.stdout.write(self.style.SUCCESS('✔ mediamtx.yml successfully generated.'))
