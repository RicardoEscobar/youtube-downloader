from pathlib import Path
import pytube
from time_it import time_it


@time_it
def download_highest_quality_audio(url: str, output: str = None) -> Path:
    """Download the highest quality audio of a YouTube video"""
    # Create a YouTube object using the URL
    yt = pytube.YouTube(url, use_oauth=True, allow_oauth_cache=True)

    # Get the highest quality audio stream
    audio_stream = yt.streams.get_by_itag(yt.streams.filter(
        only_audio=True).order_by('abr').desc().first().itag)

    # Save the audio stream to a file
    if output is None:
        output_file = Path(audio_stream.default_filename)
    else:
        output_file = Path(output)

    # Download the audio stream
    audio_stream.download(filename=output_file)

    # Return a path to the output file
    return output_file


if __name__ == '__main__':
    # Test the function with a YouTube video URL
    download_highest_quality_audio(
        'https://youtu.be/wbM7p5-cG2k')
