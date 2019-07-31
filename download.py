from __future__ import unicode_literals
import youtube_dl, asyncio, MainExceptions
def mainloop(url, tracknum):
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',}],
            'outtmpl': 'queue/'+str(tracknum)+'.%(ext)s',
            'quiet' : False,
            'max_filesize' : 41943040
            }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.extract_info(url, download=True)
        except Exception as e:
            print(e)
            ydl.extract_info("ytsearch:"+url, download = True)