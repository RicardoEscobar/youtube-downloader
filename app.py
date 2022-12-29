import tkinter as tk
import tkinter.ttk as ttk
from download_music import download_music

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")
# root.resizable(False, False)
# Set the width to 300 pixels and the height to 100 pixels
# root.geometry("300x100")

# Create a frame and pack it into the main window
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Create a frame_audio_download and pack it into the frame, with padding
frame_audio_download = tk.Frame(frame, padx=10, pady=10)
frame_audio_download.pack()

# Create a frame_progress and pack it into the frame, with padding
frame_progress = tk.Frame(frame, padx=10, pady=10)
frame_progress.pack()

# Create a text input and a button, and pack them into the frame
youtube_url_input = tk.Entry(frame_audio_download)
youtube_url_input.pack(side='left')
download_button = tk.Button(frame_audio_download, text='Download', command=lambda: download_music(
    youtube_url_input.get()))  # Retrieve the text from the text_input widget)
download_button.pack(side='left')

# Create a progress bar and pack it into the frame
progress_bar = ttk.Progressbar(frame_progress, orient='horizontal', length=300)
progress_bar.pack(side='top')

# Run the Tkinter event loop
root.mainloop()
