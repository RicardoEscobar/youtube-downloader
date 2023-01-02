from pathlib import Path
import tkinter as tk
import tkinter.ttk as ttk
import pytube
from time_it import time_it
from update_progress_bar import update_progress_bar


@time_it
def download_video(url: str, progress_bar_variable: tk.IntVar = None, progress_bar: ttk.Progressbar = None) -> None:
    print(
        f'download_video:progress_bar_variable -> {progress_bar_variable.get()}')
    # Create a YouTube object using the URL, add progress_bar_variable if able
    yt = pytube.YouTube(
        url,
        on_progress_callback=lambda stream, chunk, bytes_remaining:
        # Lambda used to pass the progress_bar_variable argument to update_progress_bar function
        update_progress_bar(stream=stream,
                            chunk=chunk,
                            bytes_remaining=bytes_remaining,
                            progress_bar_variable=progress_bar_variable,
                            progress_bar=progress_bar
                            )
    )

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
