import pytube
import tkinter as tk
import tkinter.ttk as ttk


# Create a function to update the progress bar
def complete_progress_bar(
        stream: pytube.Stream,
        file_handle,
        progress_bar_variable: tk.IntVar = None,
        progress_bar: ttk.Progressbar = None):

    # Initialize progress_bar_variable
    if progress_bar_variable:
        progress_bar_variable.initialize(0)

    # Refresh the display of the progress bar
    if progress_bar:
        progress_bar.update()
