from time_it import time_it
import tkinter as tk
import tkinter.ttk as ttk
from download_highest_quality_audio import download_highest_quality_audio
from convert_to_mp3 import convert_to_mp3


@time_it
def download_audio(url: str, progress_bar_variable: tk.IntVar = None, progress_bar: ttk.Progressbar = None) -> None:
    audio = download_highest_quality_audio(
        url, progress_bar_variable=progress_bar_variable, progress_bar=progress_bar)
    output = audio.with_name(audio.stem + ' (prime audio)' + '.mp3')

    # Convert downloaded audio file into mp3 file
    convert_to_mp3(audio, output)

    # clean up
    audio.unlink()


if __name__ == '__main__':
    # Replace this with the URL of the YouTube video you want to download
    download_audio("https://youtu.be/qpCNaRkIh2E")
