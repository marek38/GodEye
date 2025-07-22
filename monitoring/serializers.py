from rest_framework import serializers
from .models import Camera, Stream, Alert, AIModel, Storage, SystemSetting, SupportTicket

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'

class StreamSerializer(serializers.ModelSerializer):
    camera = CameraSerializer(read_only=True)
    class Meta:
        model = Stream
        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    camera = CameraSerializer(read_only=True)
    class Meta:
        model = Alert
        fields = '__all__'

class AIModelSerializer(serializers.ModelSerializer):
    cameras = CameraSerializer(many=True, read_only=True)
    class Meta:
        model = AIModel
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class SystemSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetting
        fields = '__all__'

class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = '__all__'