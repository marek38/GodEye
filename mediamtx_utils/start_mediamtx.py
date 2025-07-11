import subprocess
import os
import socket

def is_port_open(port, host="localhost"):
    """Skontroluj, či je port otvorený (teda či MediaMTX už beží)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        return sock.connect_ex((host, port)) == 0

def start_mediamtx():
    # Uprav si tieto cesty podľa potreby
    mediamtx_path = os.path.abspath("./mediamtx")  # alebo absolútna cesta k binárke
    config_path = os.path.abspath("mediamtx.yml")

    rtsp_port = 8554  # defaultný RTSP port MediaMTX

    if is_port_open(rtsp_port):
        print("ℹ️ MediaMTX už beží (port 8554 je otvorený).")
        return

    try:
        subprocess.Popen(
            [mediamtx_path, "--config", config_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("MediaMTX server bol spustený.")
    except Exception as e:
        print(f"Chyba pri spúšťaní MediaMTX: {e}")
