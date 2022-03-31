#Python – Downloading captions from YouTube
#youtube_transcript_api: This module is used for getting the captions/subtitles from a YouTube Video. It can be installed using:
#pip install youtube-transcript-api

#Before starting with the process we would like to explain how we can get the video id of a YouTube video. For Example, if a YouTube video has the following URL

#https://youtu.be/SW14tOda_kI
#Then the video id for this video would be “SW14tOda_kI”, i.e. all the phrases after the ?v= counts as the video id. This is unique for each video on YouTube.

from youtube_transcript_api import YouTubeTranscriptApi

# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
srt = YouTubeTranscriptApi.get_transcript("JdIykKy0Vfo")

# prints the result
#print(srt)

# creating or overwriting a file "subtitles.txt" with
# the info inside the context manager
with open("subtitles.txt", "w") as f:
   
        # iterating through each element of list srt
    for i in srt:
        # writing each element of srt on a new line
        f.write("{}\n".format(i))
