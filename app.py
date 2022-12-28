import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")
root.resizable(False, False)

# Create a frame and pack it into the main window
frame = tk.Frame(root)
frame.pack()

# Create a text input and a button, and pack them into the frame
youtube_url_input = tk.Entry(frame)
youtube_url_input.pack(side='left')
download_button = tk.Button(frame, text='Download')
download_button.pack(side='left')

# Run the Tkinter event loop
root.mainloop()
