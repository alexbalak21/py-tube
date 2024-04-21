from pytube import YouTube

# AUDIO 
# stream  = YouTube('https://music.youtube.com/watch?v=YWEUzzHb7MU').streams.filter(only_audio=True).order_by('abr').desc()
stream  = YouTube('https://music.youtube.com/watch?v=YWEUzzHb7MU').streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
video = stream.first()
path = video.download(output_path="./downloads/", filename='monstares.mp4' )
path = path.replace("\\./", "\\")
path = path.replace("\\", "/")
