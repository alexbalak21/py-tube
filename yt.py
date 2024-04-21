from pytube import YouTube
from converter import convert_video_to_audio

def get_video_from_tube(url='https://music.youtube.com/watch?v=YWEUzzHb7MU')->str:
    # AUDIO 
    # stream  = YouTube('https://music.youtube.com/watch?v=YWEUzzHb7MU').streams.filter(only_audio=True).order_by('abr').desc()
    # VIDEO
    stream  = YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    video = stream.first()
    path = video.download(output_path="./downloads/")
    path = path.replace("\\./", "\\")
    path = path.replace("\\", "/")
    return path

path = get_video_from_tube()
convert_video_to_audio(path)
