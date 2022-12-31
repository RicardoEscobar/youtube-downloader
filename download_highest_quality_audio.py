from pathlib import Path
import pytube
from time_it import time_it
from convert_to_mp3 import convert_to_mp3


@time_it
def download_highest_quality_audio(url: str) -> None:
    """Download the highest quality audio of a YouTube video"""
    # Create a YouTube object using the URL
    yt = pytube.YouTube(url)

    # Get the highest quality audio stream
    audio_stream = yt.streams.get_by_itag(yt.streams.filter(
        only_audio=True).order_by('abr').desc().first().itag)

    # Save the audio stream to a file
    output_file = Path(audio_stream.default_filename)
    print(output_file)
    audio_stream.download(filename=output_file)


if __name__ == '__main__':
    # Test the function with a YouTube video URL
    download_highest_quality_audio(
        'https://youtu.be/qpCNaRkIh2E')
    input_file = Path('She Knows - J Cole  Español.webm')
    output_file = Path('She Knows - J Cole  Español.mp3')
    convert_to_mp3(input_file, output_file)
