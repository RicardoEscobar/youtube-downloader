from pathlib import Path
import pytube
from time_it import time_it


@time_it
def download_audio(url: str) -> None:
    # Create a YouTube object using the URL
    yt = pytube.YouTube(url)

    # Get the highest quality audio stream available
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Save the audio stream to a file
    output_file = Path(audio_stream.default_filename).with_suffix('.mp3')
    print(output_file)
    audio_stream.download(filename=output_file)


if __name__ == '__main__':
    # Replace this with the URL of the YouTube video you want to download
    download_audio("https://youtu.be/qpCNaRkIh2E")
