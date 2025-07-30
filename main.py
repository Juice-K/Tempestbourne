# main.py

import csv
import random
import os
from dotenv import load_dotenv
import matplotlib as plt
plt.use('TkAgg')  # Use TkAgg backend for matplotlib
import seaborn as sns
import tkinter as tk
from tkinter import ttk, messagebox
from gui.input_form import InputForm   
from gui.results_display import CharacterResultsFrame, WeatherComparisonFrame   # GUI components for displaying results
from features.character_generator import generate_character
from features.weather_fetcher import get_weather_data_for_city, get_random_city


load_dotenv() # Load environment variables

# --- Custom GUI Theme ---
style = ttk.Style() # Use default theme
style.theme_use("default") # Set the default theme


# --- Helper: Get Inspirational Quote ---
def get_random_quote():
    try:
        with open(os.path.join("utils", "weather_quotes.csv"), newline='') as csvfile:
            quotes = [row[0] for row in csv.reader(csvfile) if row]
        return random.choice(quotes) if quotes else ""
    except Exception as e:
        print(f"[Quote Error] {e}")
        return "Forge ahead – every storm makes a stronger hero."

# --- App Setup ---
root = tk.Tk()
root.title("Tempestbourne: Weather-Forged Adventurers")

# Container for form and buttons
main_container = ttk.Frame(root)
main_container.pack(padx=20, pady=20, fill="both", expand=True)

# --- Inspirational Quote ---
quote_var = tk.StringVar(value=get_random_quote())
quote_label = ttk.Label(
    main_container,
    textvariable=quote_var,
    wraplength=500,
    justify="center",
    font=("Helvetica", 10, "italic")
)
quote_label.pack(pady=(0, 10))

# Scrollable results container
results_container_frame = ttk.Frame(main_container)
results_container_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(results_container_frame)
scrollbar = ttk.Scrollbar(results_container_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Bind mouse wheel for scrolling
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

scrollable_frame.bind_all("<MouseWheel>", _on_mousewheel)


# --- Form Submission Handler ---
def handle_form_submission(form_data):
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

    # 🧹 Clear old results
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    # 🖼️ Display weather comparison    
    ttk.Label(scrollable_frame, text="🌍 Weather Comparison", font=("Helvetica", 12, "bold")).pack(pady=(20, 0))
    WeatherComparisonFrame(
        scrollable_frame,
        weather1=weather_user,
        weather2=weather_random,
        city1=city,
        city2=random_city
    ).pack(pady=10, fill="both", expand=True)


    # alter theme by weather results
    def apply_weather_theme(condition):
        if not isinstance(condition, str):  # Ensure condition is a string
            return  # or log it and return  

        condition = condition.lower()  # Normalize condition to lowercase to avoid crashes

        if "rain" in condition:
            style.configure("TFrame", background="#dce3f0") # Light blue for rainy weather
            style.configure("TLabel", background="#dce3f0")
        elif "clear" in condition:
            style.configure("TFrame", background="#fff9e6") # Light cream for clear weather
            style.configure("TLabel", background="#fff9e6")
        elif "cloud" in condition:
            style.configure("TFrame", background="#e6e6e6") # Light gray for cloudy weather
            style.configure("TLabel", background="#e6e6e6")
        elif "storm" in condition:
            style.configure("TFrame", background="#f0f0f07f") # Light gray for stormy weather
            style.configure("TLabel", background="#f0f0f07f")
        elif "snow" in condition:
            style.configure("TFrame", background="#84D2F9") # Light blue for snowy weather
            style.configure("TLabel", background="#84D2F9")
        elif "thunderstorm" in condition:
            style.configure("TFrame", background="#5e0770") # Dark purple for stormy weather
            style.configure("TLabel", background="#5e0770")
        else:
            style.configure("TFrame", background="#f5f5f5") # light gray background
            style.configure("TLabel", background="#f5f5f5")

    main_condition = weather_user.get("weather", [{}])[0].get("main", "") # Get the main weather condition
    apply_weather_theme(main_condition)                                   # Apply the theme based on the main condition

    # 🖼️ Display results in a scrollbox
    ttk.Label(scrollable_frame, text=f"🌆 {city} Adventurer", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
    CharacterResultsFrame(scrollable_frame, character=char_user).pack(pady=10)

    ttk.Label(scrollable_frame, text=f"🧭 Random City: {random_city}", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
    CharacterResultsFrame(scrollable_frame, character=char_random).pack(pady=10)

    # 🌟 Update quote
    quote_var.set(get_random_quote())

# --- Reset Handler ---
def reset_app():
    form.reset()
    quote_var.set(get_random_quote())
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

# --- Form UI ---
form = InputForm(main_container, on_submit_callback=handle_form_submission)
form.pack(pady=(0, 10))

# --- Buttons ---
button_frame = ttk.Frame(main_container)
button_frame.pack(pady=(0, 10))

generate_btn = ttk.Button(button_frame, text="Generate Character", command=lambda: handle_form_submission(form.get_form_data()))
generate_btn.grid(row=0, column=0, padx=5)

reset_btn = ttk.Button(button_frame, text="Reset", command=reset_app)
reset_btn.grid(row=0, column=1, padx=5)

# --- Bind Return Key ---
root.bind("<Return>", lambda event: handle_form_submission(form.get_form_data()))


# Base colors
base_bg = "#f5f5f5"
accent_color = "#6a5acd"  # Slate blue
highlight_color = "#ffcc00"  # Gold

# General styling
style.configure("TFrame", background=base_bg)
style.configure("TLabel", background=base_bg, font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10, "bold"), padding=6)
style.configure("TScrollbar", troughcolor=accent_color, background=highlight_color)

# Scrollbar active hover
style.map("TScrollbar", background=[("active", highlight_color)])

# Quote tweak
quote_label.configure(foreground="#333333")

# ensure the code is getting to this point
print("App launching...")

# --- Run App ---
if __name__ == "__main__":
    try:
        root.mainloop()
    except Exception as e:
        print(f"[Main Error] {e}")