from pytube import YouTube

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

