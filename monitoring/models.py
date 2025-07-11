# models.py

from django.db import models

class Camera(models.Model):
    name = models.CharField(max_length=100)
    host = models.GenericIPAddressField()
    port = models.PositiveIntegerField(default=554)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    stream_path = models.CharField(max_length=200)  # napr. /stream1

    def __str__(self):
        return self.name

class GlobalSettings(models.Model):
    server_rtsp_enabled = models.BooleanField(default=True)
    server_rtmp_enabled = models.BooleanField(default=False)
    log_level = models.CharField(max_length=10, default="info")  # debug/info/warn/error

    def __str__(self):
        return "Global Settings"
