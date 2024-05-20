import tkinter as tk
from tkinter import filedialog, ttk
import pygame
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")

        self.playlist = []
        self.current_track_index = 0

        # Create GUI elements
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.controls_frame = ttk.Frame(master)
        self.controls_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        self.play_button = ttk.Button(self.controls_frame, text="▶ Play", command=self.play)
        self.pause_button = ttk.Button(self.controls_frame, text="❚❚ Pause", command=self.pause)
        self.stop_button = ttk.Button(self.controls_frame, text="■ Stop", command=self.stop)
        self.next_button = ttk.Button(self.controls_frame, text="► Next", command=self.next_track)
        self.prev_button = ttk.Button(self.controls_frame, text="◄ Previous", command=self.prev_track)
        self.add_button = ttk.Button(self.controls_frame, text="➕ Add", command=self.add_to_playlist)

        self.play_button.grid(row=0, column=0, padx=(0, 5))
        self.pause_button.grid(row=0, column=1, padx=(0, 5))
        self.stop_button.grid(row=0, column=2, padx=(0, 5))
        self.prev_button.grid(row=0, column=3, padx=(0, 5))
        self.next_button.grid(row=0, column=4, padx=(0, 5))
        self.add_button.grid(row=0, column=5)

        self.playlist_frame = ttk.Frame(master)
        self.playlist_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

        self.playlist_listbox = tk.Listbox(self.playlist_frame, selectmode=tk.SINGLE, height=15, width=50)
        self.playlist_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.playlist_frame, orient="vertical", command=self.playlist_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.playlist_listbox.config(yscrollcommand=self.scrollbar.set)

        # Initialize pygame
        pygame.init()
        pygame.mixer.init()

    def add_to_playlist(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_paths:
            for file_path in file_paths:
                self.playlist.append(file_path)
                filename = os.path.basename(file_path)
                self.playlist_listbox.insert(tk.END, filename)

    def play(self):
        if not pygame.mixer.music.get_busy() and self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track_index])
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if self.playlist:
            self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
            self.play()

    def prev_track(self):
        if self.playlist:
            self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
            self.play()

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
