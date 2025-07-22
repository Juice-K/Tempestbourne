# Main

from features.gif_selector import generate_gif_prompt, generate_gif_from_prompt
import tkinter as Tk 
from tkinter import ttk
from gui.gif_preview_frame import GifPreviewFrame 
from gui.results_display import CharacterResultsFrame
from features.character_generator import generate_character
from features.weather_fetcher import get_sample_weather_data

# first version character display gui (ChatGPT)
root = Tk()
root.title("Character Sheet")

# Simulate a weather pull and character gen
weather_data = get_sample_weather_data()
char_obj = generate_character(weather_data, level=3, gender="Male")

# Display character results
results_frame = CharacterResultsFrame(root, character=char_obj)
results_frame.pack(padx=20, pady=20)

root.mainloop()


#  placeholder gui for GIF generation (ChatGPT)
root = Tk()
root.title("Tempestbourne Character Viewer")

# Preview a placeholder gif
gif_frame = GifPreviewFrame(root, gif_path="assets/gifs/placeholder.gif")
gif_frame.pack(padx=20, pady=20)

root.mainloop()


#  Placeholder character data for testing (ChatGPT)
example_character = {
    "race": "Half-Orc",
    "class": "Barbarian",
    "alignment": "Chaotic Good",
    "traits": ["stormy", "wild", "unyielding"],
    "equipment": {
        "weapons": ["greataxe", "javelin"]
    },
    "level": 5
}

prompt = generate_gif_prompt(example_character)
gif_path = generate_gif_from_prompt(prompt)
print("GIF saved or hosted at:", gif_path)
