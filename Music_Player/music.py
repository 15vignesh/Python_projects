import tkinter as tk
import pygame
from tkinter import filedialog

def play_music():
    try:
        file_path = file_path_entry.get()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print("Error occurred while playing the music:", str(e))

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def set_volume(volume):
    pygame.mixer.music.set_volume(volume)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=(("Audio files", "*.mp3"), ("All files", "*.*")))
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(tk.END, file_path)

# Initialize pygame mixer
pygame.mixer.init()

# Create the main window
window = tk.Tk()
window.title("Music Player")

# Create the file path entry
file_path_entry = tk.Entry(window, width=50)
file_path_entry.pack()

# Create the browse button
browse_button = tk.Button(window, text="Browse", command=browse_file, width=10, height=2)
browse_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the play button
play_button = tk.Button(window, text="Play", command=play_music, width=10, height=2)
play_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the pause button
pause_button = tk.Button(window, text="Pause", command=pause_music, width=10, height=2)
pause_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the resume button
resume_button = tk.Button(window, text="Resume", command=resume_music, width=10, height=2)
resume_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the stop button
stop_button = tk.Button(window, text="Stop", command=stop_music, width=10, height=2)
stop_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the volume scale
volume_label = tk.Label(window, text="Volume")
volume_label.pack()

volume_scale = tk.Scale(window, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=set_volume)
volume_scale.set(0.5)
volume_scale.pack()

# Run the GUI main loop
window.mainloop()