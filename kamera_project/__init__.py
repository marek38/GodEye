import os
import subprocess

def run_ffmpeg_streams():
    script_path = os.path.join(os.path.dirname(__file__), 'monitoring', 'start_streams.sh')
    if os.path.exists(script_path):
        subprocess.Popen(['bash', script_path])

run_ffmpeg_streams()
