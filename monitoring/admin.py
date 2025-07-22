from django.contrib import admin
from .models import Camera, Stream, Alert, AIModel, Storage, SystemSetting, SupportTicket


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('name', 'rtsp_url', 'zone', 'created_at')
    list_filter = ('zone',)

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('camera', 'rtsp_url', 'status', 'last_active')
    list_filter = ('status',)
    search_fields = ('camera__name', 'rtsp_url')

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('camera', 'alert_type', 'severity', 'timestamp', 'status')
    list_filter = ('alert_type', 'severity', 'status')
    search_fields = ('camera__name', 'description')

@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'category', 'accuracy', 'status')
    list_filter = ('category', 'status')
    search_fields = ('name', 'version')

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'total_space', 'used_space', 'status')
    list_filter = ('type', 'status')
    search_fields = ('name',)

@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'updated_at')
    search_fields = ('key', 'value')

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'priority', 'status', 'created_at')
    list_filter = ('priority', 'status')
    search_fields = ('subject', 'description')