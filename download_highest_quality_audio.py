from pathlib import Path
import tkinter as tk
import tkinter.ttk as ttk
import pytube
from time_it import time_it
from update_progress_bar import update_progress_bar
from complete_progress_bar import complete_progress_bar


@time_it
def download_highest_quality_audio(url: str, progress_bar_variable: tk.IntVar = None, progress_bar: ttk.Progressbar = None) -> Path:
    """Download the highest quality audio of a YouTube video"""
    # Create a YouTube object using the URL
    yt = pytube.YouTube(
        url=url,
        on_progress_callback=lambda stream, chunk, bytes_remaining:
        # Lambda used to pass the progress_bar_variable argument to update_progress_bar function
        update_progress_bar(stream=stream,
                            bytes_remaining=bytes_remaining,
                            progress_bar_variable=progress_bar_variable,
                            progress_bar=progress_bar
                            ),
        on_complete_callback=lambda stream, file_handle:
        complete_progress_bar(
            stream=stream,
            file_handle=file_handle,
            progress_bar_variable=progress_bar_variable,
            progress_bar=progress_bar)
    )

    # Get the highest quality audio stream
    audio_stream = yt.streams.get_by_itag(yt.streams.filter(
        only_audio=True).order_by('abr').desc().first().itag)

    # Save the audio stream to a file
    output_file = Path(audio_stream.default_filename)
    print(output_file)
    audio_stream.download(filename=output_file)

    # Return a path to the output file
    return output_file


if __name__ == '__main__':
    # Test the function with a YouTube video URL
    download_highest_quality_audio(
        'https://youtu.be/wbM7p5-cG2k')
