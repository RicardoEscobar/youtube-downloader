import threading
import tkinter as tk
import tkinter.ttk as ttk
from download_highest_quality_audio import download_highest_quality_audio
from convert_to_mp3 import convert_to_mp3
from time_it import time_it


@time_it
def download_audio(url: str, progress_bar_variable: tk.IntVar = None, progress_bar: ttk.Progressbar = None) -> None:
    """Downloads audio from a YouTube url as MP3 file.

    Args:
        url (str): The url to the YouTube video.
        progress_bar_variable (tkinter.IntVar, Optional): Variable for completion percentage.
        progress_bar (ttk.Progressbar, Optional): Progress bar to be used to display progress or activity.

    Returns:
        None
    """
    # Run the download_highest_quality_audio function in a separate thread
    thread = threading.Thread(target=download_highest_quality_audio, args=(
        url, progress_bar_variable, progress_bar))
    thread.start()

    # Wait for the thread to finish
    thread.join()

    # Convert downloaded audio file into mp3 file.
    # convert_to_mp3(input_file, output_file)

    # clean up
    # input_file.unlink()


if __name__ == '__main__':
    # Replace this with the URL of the YouTube video you want to download.
    download_audio("https://youtu.be/qpCNaRkIh2E")
