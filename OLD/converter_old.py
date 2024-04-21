import subprocess

def convert_video_to_audio(video_file_path, audio_file_path):
    command = "ffmpeg -i {} -vn -ar 44100 -ac 2 -b:a 192k {}".format(video_file_path, audio_file_path)
    subprocess.call(command, shell=True)

