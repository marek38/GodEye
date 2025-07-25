from django.apps import AppConfig
import subprocess
import os

# class MonitoringConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'monitoring'

#     def ready(self):
#         # Absolútna cesta ku skriptu
#         script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'start_streams.py')

#         if os.path.exists(script_path):
#             try:
#                 subprocess.Popen(['python3', script_path])
#                 print("▶️ Aktivovaný skript na štart streamov.")
#             except Exception as e:
#                 print("❌ Chyba pri spúšťaní skriptu:", e)

# napr. v kamera/apps.py

from django.apps import AppConfig
import threading

class MonitoringConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitoring'

    def ready(self):
        import monitoring.signals
        from mediamtx_utils.start_mediamtx import start_mediamtx
        threading.Thread(target=start_mediamtx).start()

