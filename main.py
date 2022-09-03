from pytube import YouTube
from sys import argv

link = argv[1] # get the input from user

yt = YouTube(link) #gets the video data for the link given


print("Title: ", yt.title)
print("Video id", yt.video_id)
print("Publish date", yt.publish_date)

vd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
vd.download('./YTfolder')


