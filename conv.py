from moviepy.editor import VideoFileClip

# Load the mp4 file
video = VideoFileClip("monsters.mp4")

# Extract audio from video
video.audio.write_audiofile("monsters.mp3")