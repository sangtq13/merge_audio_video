from moviepy.editor import *
import os
from natsort import natsorted

L = []

for root, dirs, files in os.walk("./"):
    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            print(filePath)
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L, method='compose')
final_clip.set_audio(AudioFileClip("audio1.mp3"))
final_clip.write_videofile("output_audio_video.mp4", codec='libx264', 
                     audio_codec='aac', 
                     temp_audiofile='temp-audio.m4a', 
                     remove_temp=True)
