from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Pridaný import

class Camera(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)
    resolution = models.CharField(max_length=20, default="1920x1080")
    fps = models.IntegerField(default=30)
    zone = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[("online", "Online"), ("offline", "Offline")], default="online")
    motion_detection = models.BooleanField(default=True)
    recording = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)  # Teraz funguje

    def __str__(self):
        return self.name

class Stream(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    rtsp_url = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[("live", "Live"), ("offline", "Offline")], default="live")
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stream for {self.camera.name}"

class Alert(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=50, choices=[
        ("motion", "Motion Detection"),
        ("person", "Person Detection"),
        ("vehicle", "Vehicle Detection"),
        ("object", "Object Detection"),
    ])
    severity = models.CharField(max_length=20, choices=[
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ("new", "New"),
        ("acknowledged", "Acknowledged"),
        ("resolved", "Resolved"),
    ], default="new")

    def __str__(self):
        return f"{self.alert_type} - {self.camera.name}"

class AIModel(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=10)
    category = models.CharField(max_length=50, choices=[
        ("detection", "Object Detection"),
        ("recognition", "Face Recognition"),
        ("behavior", "Behavior Analysis"),
        ("vehicle", "Vehicle Detection"),
        ("crowd", "Crowd Analysis"),
    ])
    accuracy = models.FloatField()
    performance = models.IntegerField()  # FPS
    compatibility = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ("active", "Active"),
        ("inactive", "Inactive"),
    ], default="active")
    cameras = models.ManyToManyField(Camera, related_name="ai_models")

    def __str__(self):
        return f"{self.name} v{self.version}"

class Storage(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[
        ("primary", "Primary"),
        ("backup", "Backup"),
        ("cloud", "Cloud"),
    ])
    total_space = models.FloatField()  # in TB
    used_space = models.FloatField()  # in TB
    status = models.CharField(max_length=20, choices=[
        ("healthy", "Healthy"),
        ("warning", "Warning"),
        ("critical", "Critical"),
    ], default="healthy")

    def __str__(self):
        return self.name

class SystemSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key

class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    priority = models.CharField(max_length=20, choices=[
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("urgent", "Urgent"),
    ])
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("closed", "Closed"),
    ], default="open")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject