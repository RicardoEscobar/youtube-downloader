from pathlib import Path
import pytube
from time_it import time_it


@time_it
def download_highest_resolution_video(url: str) -> Path:
    """Download the highest resolution DASH stream of a YouTube video"""
    # Create a YouTube object using the URL
    yt = pytube.YouTube(url)

    # Get the highest resolution DASH stream
    dash_stream = yt.streams.get_by_itag(yt.streams.filter(
        adaptive=True).order_by('filesize').desc().first().itag)

    # Download the DASH stream
    output_file = Path(dash_stream.default_filename)
    dash_stream.download(filename=output_file)

    # Return a path to the output file
    return output_file


if __name__ == '__main__':
    # Test the function with a YouTube video URL
    download_highest_resolution_video(
        'https://youtu.be/wbM7p5-cG2k')
