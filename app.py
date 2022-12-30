import tkinter as tk
import tkinter.ttk as ttk
from download_music import download_music
import windows

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")
# root.resizable(False, False)
# Set the width to 300 pixels and the height to 100 pixels
# root.geometry("300x100")

# Create a frame and pack it into the main window
frame = tk.Frame(root, padx=10, pady=10, bg='red')
frame.pack(expand=True, fill='both')

# Create a frame_audio_download and pack it into the frame, with padding
frame_audio_download = tk.Frame(frame, padx=10, pady=10)
frame_audio_download.pack(expand=True, fill='x')

# Create a frame_progress and pack it into the frame, with padding
frame_progress = tk.Frame(frame, padx=10, pady=10)
frame_progress.pack(expand=True, fill='x')

# Create a text input and a button, and pack them into the frame
youtube_url_input = tk.Entry(frame_audio_download)
# Set the sticky attribute to 'ew' to make the text input expand horizontally
youtube_url_input.pack(side='left', fill='x', expand=True)
download_button = tk.Button(frame_audio_download, text='Download', command=lambda: download_music(
    youtube_url_input.get()))  # Retrieve the text from the text_input widget)
download_button.pack(side='right')

# Create a progress bar and pack it into the frame
progress_bar = ttk.Progressbar(frame_progress, orient='horizontal', length=300)
progress_bar.pack(side='left', fill='x', expand=True)

# Run the Tkinter event loop
root.mainloop()
