from pathlib import Path
import pytube
from time_it import time_it


@time_it
def download_video(url: str) -> None:
    # Create a YouTube object using the URL
    yt = pytube.YouTube(url)

    # Get the list of available streams
    streams = yt.streams.filter(progressive=True)

    # Get the stream with the highest resolution
    video = streams.order_by("resolution").desc().first()

    # Download the video
    output_file = Path(video.default_filename)
    print(output_file)
    video.download(filename=output_file)


if __name__ == '__main__':
    # Replace this with the URL of the YouTube video you want to download
    download_video("https://youtu.be/qpCNaRkIh2E")
