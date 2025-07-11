import os
import subprocess
import signal
import sys
import time

mediamtx_process = None

def start_mediamtx():
    global mediamtx_process
    if mediamtx_process is None:
        mediamtx_path = os.path.join(os.getcwd(), 'mediamtx')
        config_path = os.path.join(os.getcwd(), 'mediamtx.yml')

        if not os.path.isfile(mediamtx_path):
            print("Chyba: mediamtx binary sa nenašiel.")
            return

        if not os.path.isfile(config_path):
            print("Chyba: mediamtx.yml sa nenašiel.")
            return

        mediamtx_process = subprocess.Popen(
            [mediamtx_path, config_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print("✅ MediaMTX bol spustený.")
    else:
        print("⚠️ MediaMTX už beží.")

def stop_mediamtx():
    global mediamtx_process
    if mediamtx_process:
        mediamtx_process.terminate()
        mediamtx_process.wait()
        print("🛑 MediaMTX bol ukončený.")

def run():
    try:
        start_mediamtx()
        # Spusti Django server
        subprocess.call(["python", "manage.py", "runserver"])
    except KeyboardInterrupt:
        print("CTRL+C zistené.")
    finally:
        stop_mediamtx()

if __name__ == "__main__":
    run()
