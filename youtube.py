#pip install pytube
from pytube import YouTube
link = "https://youtu.be/iMplmIVcXqs"
yt = YouTube(link)
#yt.streams.first().download()
video_file = yt.streams.filter(file_extension="mp4")
d_files = video_file.get_by_resolution("720p").download()

