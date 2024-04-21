from moviepy.editor import VideoFileClip


def convert_video_to_audio(file_path:str, title:str):
    # Load the mp4 file
    video = VideoFileClip(file_path)
    # Extract audio from video
    video.audio.write_audiofile(filename=f'./audio/{title}.mp3', bitrate="160k", verbose=False)
    video.close()