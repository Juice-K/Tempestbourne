# gui/gif_preview_frame.py

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
import os

class GifPreviewFrame(tk.Frame):
    def __init__(self, parent, gif_path="assets/gifs/placeholder.gif", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.gif_path = gif_path
        self.frames = []
        self.label = tk.Label(self)
        self.label.pack()

        self.load_gif()
        self.current_frame_index = 0
        self.after_id = None
        self.animate()

    def load_gif(self):
        """Load GIF frames from file."""
        if not os.path.exists(self.gif_path):
            self.label.config(text="GIF not found.")
            return
        
        gif = Image.open(self.gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

    def animate(self):
        """Loop through GIF frames."""
        if not self.frames:
            return

        self.label.config(image=self.frames[self.current_frame_index])
        self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
        self.after_id = self.after(100, self.animate)

    def update_gif(self, new_path):
        """Replace the current GIF with a new one."""
        self.gif_path = new_path
        self.frames.clear()
        self.load_gif()
        self.current_frame_index = 0
