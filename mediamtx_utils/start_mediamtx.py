import subprocess
import os
import socket
from django.conf import settings
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_port_open(port, host="localhost"):
    """Skontroluj, či je port otvorený (teda či MediaMTX už beží)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2)
        return sock.connect_ex((host, port)) == 0

def start_mediamtx():
    # Dynamická cesta k binárke a konfigurácii
    mediamtx_path = os.path.join(settings.BASE_DIR, "mediamtx")
    config_path = os.path.join(settings.BASE_DIR, "mediamtx.yml")

    webrtc_port = 8889  # Port pre WebRTC namiesto RTSP 8554

    # Kontrola existencie súborov
    if not os.path.exists(mediamtx_path):
        logger.error(f"Binárka MediaMTX nebola nájdená na ceste: {mediamtx_path}")
        return
    if not os.path.exists(config_path):
        logger.error(f"Konfiguračný súbor mediamtx.yml nebol nájdený na ceste: {config_path}")
        return

    if is_port_open(webrtc_port):
        logger.info(f"ℹ️ MediaMTX už beží (port {webrtc_port} je otvorený).")
        return

    try:
        logger.info(f"Spúšťam MediaMTX s konfiguráciou: {config_path}")
        process = subprocess.Popen(
            [mediamtx_path, "--config", config_path],
            cwd=settings.BASE_DIR,  # alebo napr. cwd="/home/godeye/kamera_project"
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Krátke čakanie na inicializáciu
        time.sleep(2)
        if is_port_open(webrtc_port):
            logger.info("MediaMTX server bol spustený úspešne.")
        else:
            logger.error(f"MediaMTX sa nepodarilo spustiť (port {webrtc_port} nie je otvorený).")
    except Exception as e:
        logger.error(f"Chyba pri spúšťaní MediaMTX: {e}")