import tkinter as tk
import tkinter.ttk as ttk
from download_audio import download_audio
from download_video import download_video
from download_prime import download_prime
from windows import windows_dpi_awareness

# Set dpi Awareness on windows 10
windows_dpi_awareness()

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")
# root.resizable(False, False)
# Set the width to 300 pixels and the height to 100 pixels
# root.geometry("300x100")

# Create a int variable to store the progress bar percentage value
progress_bar_variable = tk.IntVar()

# Create a string variable to store the progress bar description text
progress_bar_label_variable = tk.StringVar()

# Initialize variables
progress_bar_variable.initialize(0)
progress_bar_label_variable.initialize('Progress %')

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
# lambda: Retrieve the text from the text_input widget to run download_audio function
download_audio_button = tk.Button(frame_audio_video_download, text='Download Audio',
                                  command=lambda: download_audio(
                                      url=youtube_url_input.get(),
                                      progress_bar_variable=progress_bar_variable,
                                      progress_bar=progress_bar))
download_video_button = tk.Button(frame_audio_video_download, text='Download Video',
                                  command=lambda: download_video(
                                      url=youtube_url_input.get(),
                                      progress_bar_variable=progress_bar_variable,
                                      progress_bar=progress_bar)
                                  )
download_prime_button = tk.Button(frame_audio_video_download, text='Download Prime',
                                  command=lambda: download_prime(url=youtube_url_input.get()))

# Add download buttons to frame_audio_video_download
download_audio_button.pack(side='right')
download_video_button.pack(side='right')
download_prime_button.pack(side='right')

# Create a progress bar and pack it into the frame
progress_bar = ttk.Progressbar(
    frame_progress,
    orient='horizontal',
    length=300,
    variable=progress_bar_variable
)
progress_bar.pack(side='left', fill='x', expand=True)


# Run the Tkinter event loop
root.mainloop()
