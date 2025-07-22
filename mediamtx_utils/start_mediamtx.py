import subprocess
import os
import socket
import sys
import logging
import time
from django.conf import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_port_open(port, host="localhost"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2)
        return sock.connect_ex((host, port)) == 0

def start_mediamtx():
    if 'makemigrations' in sys.argv or 'migrate' in sys.argv:
        logger.info("➡️ Preskakujem spustenie MediaMTX počas migrácií.")
        return

    mediamtx_path = os.path.join(settings.BASE_DIR, "mediamtx")
    config_path = os.path.join(settings.BASE_DIR, "mediamtx.yml")
    webrtc_port = 8889

    if not os.path.exists(mediamtx_path):
        logger.error(f"Binárka MediaMTX neexistuje: {mediamtx_path}")
        return

    if not os.path.exists(config_path):
        logger.error(f"Konfiguračný súbor chýba: {config_path}")
        return

    if is_port_open(webrtc_port):
        logger.info(f"✅ MediaMTX už beží (port {webrtc_port} otvorený).")
        return

    try:
        logger.info(f"Spúšťam MediaMTX s konfiguráciou: {config_path}")
        process = subprocess.Popen(
            [mediamtx_path, config_path],  # bez --config
            cwd=settings.BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(5)
        if is_port_open(webrtc_port):
            logger.info("✅ MediaMTX server bol spustený.")
        else:
            logger.error("❌ MediaMTX sa nespustil (port 8889 nie je otvorený).")
    except Exception as e:
        logger.error(f"Chyba pri spúšťaní MediaMTX: {e}")
