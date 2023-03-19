# This code for extract images from video file.

# Replace with the filenames you uploaded to the movieNsubtitle folder.
# video_filename -> Change.
# subtitles_filename -> Change.


import os
import subprocess

# video dosyası adı ve uzantısı
video_filename = 'movieNsubtitle/Taxi.Driver.1976.mkv'
subtitles_filename = 'movieNsubtitle/Taxi.Driver.English.srt'

# ffmpeg komutu
ffmpeg_cmd = f'ffmpeg -i {video_filename} -vf "subtitles={subtitles_filename}" -qscale:v 10 -r 1 -f image2 frames/frame%03d.jpg -hwaccel dxva2'

# ffmpeg işlemini başlat
ffmpeg_process = subprocess.Popen(ffmpeg_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# işlem bitene kadar devam eden gösterge
while True:
    output = ffmpeg_process.stderr.readline()
    if output == b'' and ffmpeg_process.poll() is not None:
        break
    if output:
        print(output.decode().strip())

# işlem tamamlandıktan sonra çıktıyı yakala
output, error = ffmpeg_process.communicate()
print(output.decode())
print(error.decode())
