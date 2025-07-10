# #!/bin/bash

# mkdir -p ../hls

# ffmpeg -rtsp_transport tcp -i "rtsp://admin:Pribovce_23@80.87.223.69:554/Streaming/channels/101/" \
#   -c:v libx264 -preset ultrafast -tune zerolatency \
#   -f hls -hls_time 2 -hls_list_size 3 -hls_flags delete_segments \
#   ../hls/stream1.m3u8
