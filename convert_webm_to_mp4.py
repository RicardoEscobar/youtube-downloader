import subprocess
from tkinter import ttk
from pathlib import Path


def convert_webm_to_mp4(input_file: Path, output_file: Path, progress_bar: ttk.Progressbar) -> None:
    """
    Converts an WEBM file to an MP4 file using ffmpeg.

    Parameters:
        input_file (Path): The input WEBM file.
        output_file (Path): The output MP4 file.

    Returns:
        None
    """
    # Run the ffmpeg command to convert the MP4 file to MP3
    command = f'ffmpeg -i "{input_file}" -vn -acodec libmp3lame -y "{output_file}"'
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as exception:
        print(
            f'An error occurred while running the ffmpeg command: {exception}')

    # Stop the progress bar activity
    progress_bar.stop()
