import os
import yt_dlp as youtube_dl



def download_audio(url, output_path):
    """
    Download audio from a youtube video
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        #add location of ffmpeg.exe
        'ffmpeg_location': 'C:\\FFmpeg\\bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #install choco on windows: https://chocolatey.org/install
        #if ffprobe is not installed, it will throw an error
        #install on windows: choco install ffmpeg
        #if ffmpeg is not installed, it will throw an error
        #install on windows: choco install ffmpeg
        ydl.download([url])

# Query 10 other videos that appear on the same page as the video
def query_youtube_search(path, search=""):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': "/audio/%(title)s.%(ext)s",
            # add location of ffmpeg.exe
            'ffmpeg_location': 'C:\\FFmpeg\\bin',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
            'search_query': search,
            'max_downloads': 10,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # install choco on windows: https://chocolatey.org/install
            # if ffprobe is not installed, it will throw an error
            # install on windows: choco install ffmpeg
            # if ffmpeg is not installed, it will throw an error
            # install on windows: choco install ffmpeg
            sources = ydl.extract_info("ytsearchdate10:{}".format(search), download=False)['entries']
            urls = []
            for source in sources:
                urls.append(source['webpage_url'])
            for url in urls:
                ydl.download([url])

    

    
if __name__ == "__main__":
    path = '/audio'
    #url = "https://www.youtube.com/watch?v=N9duDfWSfU4"
    output_path = os.path.join(path, "audio.wav")
    #query_youtube_search(output_path,search="Joe Rogan")
    query_youtube_search(output_path,search="20 seconds")