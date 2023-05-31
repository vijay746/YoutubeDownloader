from pytube import YouTube



def getUserLinksToDownload():
    links = open('links_file.txt', 'r')
    return links


def getYoutubeLink(link):
    yt = YouTube(link)
    return yt

#Showing details
def showVideoDetails(yt):
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    print("Rating of video: ", yt.rating)


def downloadTheSong(yt):
    # Getting the highest resolution possible
   # ys = yt.streams.get_highest_resolution()
   # ys = yt.streams.get_lowest_resolution()
   # yt.streams.filter()  # to look into its usage
    # Getting the audio from clip
    ys = yt.streams.get_audio_only()
    # Starting download
    print("Downloading...")
    ys.download()
    print("Download completed!!")

def downloadMP4Song(yt):
    # filters out all the files with "mp4" extension
    mp4files = yt.filter('mp4')
    # get the video with the extension and
    # resolution passed in the get() function
    d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
    try:
        # downloading the video
        d_video.download() #d_video.download(SAVE_PATH)
    except:
        print("Some Error!")
    print('Task Completed!')


if __name__ == '__main__':
    links = getUserLinksToDownload()
    for link in links:
        yt = getYoutubeLink(link)
        showVideoDetails(yt)
        downloadTheSong(yt)
        downloadMP4Song(yt)

