import threading
from tkinter import ttk
from convert_mp4_to_mp3 import convert_mp4_to_mp3


def start_conversion_mp4_to_mp3(input_file: str, output_file: str, progress_bar: ttk.Progressbar) -> None:
    """
    Callback function for the 'Convert' button. This function starts a new thread to run the
    convert_mp4_to_mp3 function and updates the progress bar while the conversion is taking place.

    Parameters:
        None

    Returns:
        None
    """
    # Start progress bar activity
    progress_bar.start()

    # Run the convert_mp4_to_mp3 function in a separate thread
    thread = threading.Thread(target=convert_mp4_to_mp3, args=(
        input_file, output_file, progress_bar))
    thread.start()
