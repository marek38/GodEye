from django.core.management.base import BaseCommand
from monitoring.models import Camera

class Command(BaseCommand):
    help = 'Seeds the database with predefined RTSP cameras'

    def handle(self, *args, **kwargs):
        data = [
            {
                "name": "cam1",
                "host": "192.168.25.206",
                "port": 554,
                "username": "admin",
                "password": "V14_d1m1r",
                "stream_path": "/media/video1"
            },
            {
                "name": "cam2",
                "host": "192.168.25.207",
                "port": 554,
                "username": "admin",
                "password": "V14_d1m1r",
                "stream_path": "/media/video1"
            },
            {
                "name": "cam3",
                "host": "192.168.25.208",
                "port": 554,
                "username": "admin",
                "password": "V14_d1m1r",
                "stream_path": "/media/video1"
            },
            {
                "name": "cam4",
                "host": "192.168.25.204",
                "port": 554,
                "username": "admin",
                "password": "V14_d1m1r",
                "stream_path": "/media/video1"
            },
        ]

        for entry in data:
            Camera.objects.update_or_create(name=entry["name"], defaults=entry)

        self.stdout.write(self.style.SUCCESS("✔ Database seeded with 4 cameras."))
