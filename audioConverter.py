import ffmpeg

def get_audio(inputName:str, outName:str):
    stream = ffmpeg.input(inputName)
    audio = stream.audio
    stream = ffmpeg.output(audio, outName)
    ffmpeg.run(stream)