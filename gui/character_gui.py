# gui/character_gui.py
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

class CharacterPreviewGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tempestbourne Character Preview")
        
      
        # Placeholder test character
        test_character = {
            "race": "Goliath",
            "class": "Barbarian",
            "alignment": "Chaotic Good",
            "weather": "Stormy",
            "weapon": "Lightning-charged Greataxe"
        }

# For testing
if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterPreviewGUI(root)
    root.mainloop()

