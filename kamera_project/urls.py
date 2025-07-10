from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from monitoring import views
from django.conf import settings
from django.conf.urls.static import static
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Ak chceš používať súbory zo zložky "hls" ako statické súbory
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "hls"),
]

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]

# Pridanie statických ciest
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static('/hls/', document_root=os.path.join(BASE_DIR, 'hls'))
