import pytube
import tkinter as tk
import tkinter.ttk as ttk


# Create a function to update the progress bar
def update_progress_bar(stream: pytube.Stream,
                        chunk,
                        bytes_remaining,
                        progress_bar_variable: tk.IntVar = None,
                        progress_bar: ttk.Progressbar = None):
    print(
        f'update_progress_bar:progress_bar_variable -> {progress_bar_variable.get()}')
    # Get total_size from stream in bytes
    total_size = stream.filesize

    # Calculate the percentage of the download that's completed
    percentage = round(((total_size - bytes_remaining) / total_size) * 100)
    print(f'{percentage}%')

    # Update the progress bar with the percentage
    if progress_bar_variable:
        progress_bar_variable.set(percentage)
        print(
            f'progress_bar_variable.set(percentage) -> {progress_bar_variable.get()}')

        # Refresh the display of the progress bar
        progress_bar.update()
