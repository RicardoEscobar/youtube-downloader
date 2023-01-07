import subprocess
from tkinter import ttk


def convert_mp4_to_mp3(input_file: str, output_file: str, progress_bar: ttk.Progressbar) -> None:
    """
    Converts an MP4 file to an MP3 file using ffmpeg.

    Parameters:
        input_file (Path): The input MP4 file.
        output_file (Path): The output MP3 file.

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
