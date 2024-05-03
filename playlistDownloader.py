from pytube import YouTube
from pytube import Playlist
import unicodedata
import re
import os.path


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def get_video_from_tube(url='https://music.youtube.com/watch?v=YWEUzzHb7MU')->dict:
    # AUDIO 
    # stream  = YouTube('https://music.youtube.com/watch?v=YWEUzzHb7MU').streams.filter(only_audio=True).order_by('abr').desc()
    # VIDEO
    stream  = YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    video = stream.first()
    title = video.title
    path = video.download(output_path="./downloads/")
    path = path.replace("\\./", "\\")
    path = path.replace("\\", "/")
    return {"title": title, "path": path}


def download_from_playlist(url=""):
    p = Playlist(url)
    i = 0
    for video in p.videos:
        i +=1
        filename = slugify(video.title)
        path = f'./{i} - {filename}'
        if (os.path.isfile(path)): continue
        print(f'Downloading : {video.title}')
        video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename_prefix=f'{i if i >= 10 else '0' + str(i)} - ',filename=f'{filename}.mp4')

download_from_playlist("https://www.youtube.com/watch?v=jVx0vWX3afA&list=PLtBKr2xHXZuNXWp9VzQW28U8xdWsl7B7Q")

