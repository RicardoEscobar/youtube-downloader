import pytube
import tkinter as tk
import tkinter.ttk as ttk


# Create a function to update the progress bar
def update_progress_bar(stream: pytube.Stream, chunk, bytes_remaining, progress_bar: ttk.Progressbar):
    # Get total_size from stream in bytes
    total_size = stream.filesize

    # Calculate the percentage of the download that's completed
    percentage = round(((total_size - bytes_remaining) / total_size) * 100)
    print(f'{percentage}%')

    # Update the progress bar with the percentage
    progress_bar["value"] = percentage

    # Update the progress bar with text
    progress_bar["value"] = percentage

    # Refresh the display of the progress bar
    progress_bar.update()
