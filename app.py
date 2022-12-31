import tkinter as tk
import tkinter.ttk as ttk
from download_audio import download_audio
from download_video import download_video
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
frame_audio_video_download = tk.Frame(frame, padx=10, pady=10)
frame_audio_video_download.pack(expand=True, fill='x')

# Create a frame_progress and pack it into the frame, with padding
frame_progress = tk.Frame(frame, padx=10, pady=10)
frame_progress.pack(expand=True, fill='x')

# Create a text input and a button, and pack them into the frame
youtube_url_input = tk.Entry(frame_audio_video_download)

# Set the youtube_url_input to make it expand horizontally
youtube_url_input.pack(side='left', fill='x', expand=True)

# Make download buttons for video and audio
download_audio_button = tk.Button(frame_audio_video_download, text='Download Audio', command=lambda: download_audio(
    youtube_url_input.get()))  # Retrieve the text from the text_input widget)
download_video_button = tk.Button(frame_audio_video_download, text='Download Video', command=lambda: download_video(
    youtube_url_input.get()))  # Retrieve the text from the text_input widget)

# Add download buttons to frame_audio_video_download
download_audio_button.pack(side='right')
download_video_button.pack(side='right')

# Create a progress bar and pack it into the frame
progress_bar = ttk.Progressbar(frame_progress, orient='horizontal', length=300)
progress_bar.pack(side='left', fill='x', expand=True)

# Run the Tkinter event loop
root.mainloop()
