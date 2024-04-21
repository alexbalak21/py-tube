from moviepy.editor import VideoFileClip
import os


def convert_video_to_audio(title:str, file_path:str,):
    # Load the mp4 file
    video = VideoFileClip(file_path)
    # Extract audio from video
    video.audio.write_audiofile(filename=f'./audio/{title}.mp3', bitrate="160k", verbose=False)
    video.close()
    os.remove(file_path)
    return title
    