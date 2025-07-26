# main.py

import tkinter as tk
from tkinter import ttk, messagebox
from gui.input_form import InputForm
from gui.results_display import CharacterResultsFrame
from features.character_generator import generate_character
from features.weather_fetcher import get_weather_data_for_city, get_random_city
from dotenv import load_dotenv
import csv
import random
import os

load_dotenv()

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

    # 🖼️ Display results
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

# --- Run App ---
root.mainloop()
