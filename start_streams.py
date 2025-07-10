# start_streams.py
# import subprocess

# streams = {
#     'stream1': 'rtsp://admin:V14_d1m1r@192.168.25.208:554/media/video1',
#     'stream2': 'rtsp://admin:V14_d1m1r@192.168.25.206:554/media/video1',
#     'stream3': 'rtsp://admin:V14_d1m1r@192.168.25.207:554/media/video1',
#     'stream4': 'rtsp://admin:V14_d1m1r@192.168.25.204:554/media/video1',
#     # Môžeš sem doplniť ďalšie RTSP adresy pre kamery 2-4
# }

# for i, (key, url) in enumerate(streams.items(), start=1):
#     command = [
#         'ffmpeg',   
#         '-i', url,
#         '-c:v', 'libx264',
#         '-preset', 'ultrafast',
#         '-tune', 'zerolatency',
#         '-f', 'hls',
#         '-hls_time', '2',
#         '-hls_list_size', '3',
#         '-hls_flags', 'delete_segments',
#         f'/home/godeye/kamera_project/hls/stream{i}.m3u8'
#     ]
#     subprocess.Popen(command)
