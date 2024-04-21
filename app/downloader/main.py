from downloader.yt_downloader import get_video_from_tube
from downloader.converter import convert_video_to_audio

def download_convert(url:str):
    infos = get_video_from_tube(url)
    title = infos["title"]
    path = infos["path"]
    audio_file = convert_video_to_audio(title=title, file_path=path)
    return audio_file


