from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import home_redirect
from django.views.generic.base import RedirectView



router = DefaultRouter()
router.register(r'cameras', views.CameraViewSet)
router.register(r'streams', views.StreamViewSet)
router.register(r'alerts', views.AlertViewSet)
router.register(r'ai-models', views.AIModelViewSet)
router.register(r'storage', views.StorageViewSet)
router.register(r'system-settings', views.SystemSettingViewSet)
router.register(r'support-tickets', views.SupportTicketViewSet)

urlpatterns = [
    path('', home_redirect, name='home'),
    path('api/cameras/<int:pk>/', views.update_camera, name='update_camera'),
    # path('api/cameras/<int:pk>/', update_camera, name='update_camera'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cameras/', views.cameras_view, name='cameras'),
    path('streams/', views.streams_view, name='streams'),
    path('alerts/', views.alerts_view, name='alerts'),
    path('settings/', views.settings_view, name='settings'),
    path('help/', views.help_view, name='help'),
    path('api/', include(router.urls)),
    path('api/save-settings/', views.save_settings, name='save_settings'),
]