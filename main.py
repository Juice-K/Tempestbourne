# main.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gui.input_form import InputForm
from gui.results_display import CharacterResultsFrame
from features.character_generator import generate_character
from features.weather_fetcher import get_weather_data_for_city, get_random_city
from features.gif_selector import create_animated_character_gif
from dotenv import load_dotenv
load_dotenv()


# --- App Setup ---
root = tk.Tk()
root.title("Tempestbourne: Weather-Forged Adventurers")

# Container for results (we’ll clear and repopulate it after form submission)
results_container = ttk.Frame(root)
results_container.pack(padx=20, pady=20)

# --- Form Submission Handler ---
def handle_form_submission(form_data):
    # [Same as before]
    city = form_data["city"]
    date = form_data["date"]
    time = form_data["time"]
    gender = form_data["gender"]
    level = int(form_data["level"])
    requested_datetime = f"{date} {time}"

    try:
        weather_user = get_weather_data_for_city(city, requested_datetime)
    except Exception as e:
        messagebox.showerror("Weather Error", f"Could not fetch weather for {city}.\n{e}")
        return

    random_city = get_random_city(exclude=city)
    try:
        weather_random = get_weather_data_for_city(random_city, requested_datetime)
    except Exception as e:
        print(f"[Weather Error] Failed to fetch weather for random city: {e}")
        return

    # 🎲 Generate characters
    char_user = generate_character(weather_user, level, gender)
    char_random = generate_character(weather_random, level, gender)

    # 🎞️ NEW: Generate GIFs for both
    char_user["gif_path"] = create_animated_character_gif(char_user)
    char_random["gif_path"] = create_animated_character_gif(char_random)

    # 🧹 Clear old results
    for widget in results_container.winfo_children():
        widget.destroy()

    # 🖼️ Display results (GIF path now included!)
    ttk.Label(results_container, text=f"🌆 {city} Adventurer", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
    CharacterResultsFrame(results_container, character=char_user).pack(pady=10)

    ttk.Label(results_container, text=f"🧭 Random City: {random_city}", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
    CharacterResultsFrame(results_container, character=char_random).pack(pady=10)


# --- Form UI ---
form = InputForm(root, on_submit_callback=handle_form_submission)
form.pack(padx=20, pady=(20, 10))

root.mainloop()
