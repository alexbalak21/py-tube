from moviepy.editor import VideoFileClip

# Load the mp4 file
video = VideoFileClip("monsters.mp4")

# Extract audio from video
video.audio.write_audiofile(filename="monstars.mp3", bitrate="160k", verbose=False)