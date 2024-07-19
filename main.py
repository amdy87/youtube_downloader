from pytube import YouTube
from pytube. innertube import _default_clients

_default_clients[ "ANDROID"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients[ "ANDROID_EMBED"][ "context"][ "client"]["clientVersion"] = "19.08.35"
_default_clients[ "IOS_EMBED"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"][ "context"]["client"]["clientVersion"] = "6.41"
_default_clients[ "ANDROID_MUSIC"] = _default_clients[ "ANDROID_CREATOR" ]

def progress_func(stream,data,bytes_remain):
    pass
while(True):
    yt = YouTube(input("Enter the url for the youtube video: "),on_progress_callback=progress_func)

    print("Video Title: ",yt.title)
    yd = yt.streams.get_highest_resolution()

    print("Highest Resolution found: ",yd.resolution)
    print("Video Framerate: ", yd.fps)
    print("File Size: ",yd.filesize)

    confirm = input("Would you like to download this: ")[0]

    if(confirm != 'y' and confirm != 'Y'):
        continue

    yd.download()
    print("Downloaded")

