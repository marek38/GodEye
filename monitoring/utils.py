# monitoring/utils.py

import yaml
from monitoring.models import Camera

def generate_mediamtx_config():
    subprocess.run(["pkill", "-f", "mediamtx"])
    subprocess.Popen(["./mediamtx", "mediamtx.yml"])

    """
    Generates mediamtx.yml configuration file based on current Camera objects in the DB.
    """

    config = {
        "server": {
            "protocols": ["webrtc"],
            "webrtc": {
                "listen_ip": "0.0.0.0",
                "port": 8889,
                "ice_servers": [{"urls": ["stun:stun.l.google.com:19302"]}]
            }
        },
        "streams": []
    }

    for camera in Camera.objects.all():
        config["streams"].append({
            "name": camera.name.lower().replace(" ", "-"),
            "url": camera.rtsp_url,
            "protocol": "rtsp"
        })

    # Save config to mediamtx.yml
    with open("mediamtx.yml", "w") as f:
        yaml.dump(config, f, sort_keys=False)

    print("[✓] mediamtx.yml regenerated with WebRTC stream info")
