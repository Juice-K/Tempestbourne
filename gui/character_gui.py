# gui/character_gui.py
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
from features.gif_selector import get_character_gif

class CharacterPreviewGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tempestbourne Character Preview")
        
        # Frame for the GIF
        self.gif_frame = tk.Frame(self.master)
        self.gif_frame.pack(pady=20)

        self.gif_label = Label(self.gif_frame)
        self.gif_label.pack()

        # Placeholder test character
        test_character = {
            "race": "Goliath",
            "class": "Barbarian",
            "alignment": "Chaotic Good",
            "weather": "Stormy",
            "weapon": "Lightning-charged Greataxe"
        }

        # Load GIF
        self.load_character_gif(test_character)

    def load_character_gif(self, character_data):
        gif_path = get_character_gif(character_data)

        try:
            gif_image = Image.open(gif_path)
            gif_photo = ImageTk.PhotoImage(gif_image)
            self.gif_label.config(image=gif_photo)
            self.gif_label.image = gif_photo  # Prevent garbage collection
        except Exception as e:
            print(f"Error loading GIF: {e}")
            self.gif_label.config(text="GIF could not be loaded.")

# For testing
if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterPreviewGUI(root)
    root.mainloop()

