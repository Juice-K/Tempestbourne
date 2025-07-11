import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import messagebox
from weather import get_current_weather
from storage import save_weather_data 
import random

WEATHER_CLASS_MAP = {
    "Thunderstorm": ("Half-Orc", "Barbarian"),
    "Drizzle": ("Halfling", "Druid"),
    "Rain": ("Tiefling", "Warlock"),
    "Snow": ("Goliath", "Monk"),
    "Clear": ("Elf", "Ranger"),
    "Clouds": ("Human", "Fighter"),
    "Mist": ("Half-Elf", "Sorcerer"),
    "Fog": ("Gnome", "Wizard"),
    "Haze": ("Tabaxi", "Rogue"),
    "Tornado": ("Dragonborn", "Paladin"),
    "Ash": ("Dwarf", "Cleric"),
    "Dust": ("Kenku", "Bard"),
    "Sand": ("Aarakocra", "Monk"),
    "Squall": ("Leonin", "Barbarian"),
    "Smoke": ("Fire Genasi", "Sorcerer"),
}

# a bunch of random cities
CITY_LIST = [
    "Tokyo", "Reykjavik", "Lima", "Cairo", "Moscow", "Istanbul",
    "Toronto", "Sydney", "Buenos Aires", "Cape Town", "Jakarta", "Oslo"
    "Berlin", "Madrid", "Rome", "Paris", "London", "New Delhi",
    "Beijing", "Seoul", "Bangkok", "Singapore", "Dubai",
    "Los Angeles", "New York", "Chicago", "San Francisco", "Miami",
    "Rio de Janeiro", "Sao Paulo", "Mexico City", "Havana",
    "Kuala Lumpur", "Hong Kong", "Tel Aviv", "Athens", 
]

def get_random_city(exclude):
    options = [city for city in CITY_LIST if city.lower() != exclude.lower()]
    return random.choice(options)

def fetch_and_display_weather():
    city = city_entry.get()
    raw_level = level_var.get()
    level = int(''.join(filter(str.isdigit, raw_level)))

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city.")
        return

    try:
        # User's city weather
        user_data = get_current_weather(city)
        save_weather_data(city, user_data)
        user_weather_main = user_data['weather'][0]['main']
        user_char = generate_character_from_weather(user_weather_main, level)

        # Random city weather
        random_city = get_random_city(city)
        random_data = get_current_weather(random_city)
        save_weather_data(random_city, random_data)
        random_weather_main = random_data['weather'][0]['main']
        random_char = generate_character_from_weather(random_weather_main, level)

        # Format output
        result = f"🌩️ **Your City: {user_data['name']}**\n"
        result += f"🌫️ {user_data['weather'][0]['description'].capitalize()} | "
        result += f"🌡️ {user_data['main']['temp']}°C | "
        result += f"💧 {user_data['main']['humidity']}% humidity | "
        result += f"💨 {user_data['wind']['speed']} m/s wind\n"
        result += f"🧝‍♂️ Your Adventurer: {user_char}\n\n"

        result += f"🌍 **Random City: {random_data['name']}**\n"
        result += f"🌫️ {random_data['weather'][0]['description'].capitalize()} | "
        result += f"🌡️ {random_data['main']['temp']}°C | "
        result += f"💧 {random_data['main']['humidity']}% humidity | "
        result += f"💨 {random_data['wind']['speed']} m/s wind\n"
        result += f"👤 Rival Adventurer: {random_char}"

        output_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", str(e))
        
def generate_character_from_weather(weather_main, level):
    race, char_class = WEATHER_CLASS_MAP.get(weather_main, ("Human", "Fighter"))
    name = f"{race} Level {level} {char_class}"
    return name


# GUI Setup
root = tk.Tk()
root.title("TEMPESTBOURNE Character Generator")
root.geometry("1000x600")   # subject to change (depends on wrapping)
root.configure(bg="#2f2f2f")  # dark slate background (subject to change)

# Fonts
title_font = tkFont.Font(family="Garamond", size=24, weight="bold")
label_font = tkFont.Font(family="Georgia", size=12)

# Title Label
tk.Label(
    root,
    text="⚔️ TEMPESTBOURNE ⚔️",
    font=title_font,
    fg="firebrick",
    bg="#2f2f2f"
).pack(pady=(10, 5))

# City input
tk.Label(
    root,
    text="Enter City:",
    font=label_font,
    fg="light gray",
    bg="#2f2f2f"
).pack()
city_entry = tk.Entry(root, width=30, font=label_font)
city_entry.pack(pady=5)

# Styled Level Dropdown – CHAOS MODE 🐉💀🔥
style = ttk.Style()
style.theme_use("default")

style.configure("TCombobox",
    fieldbackground="#1a1a1a",
    background="#1a1a1a",
    foreground="white",
    selectbackground="#3f3f3f",
    selectforeground="white",
    arrowcolor="firebrick",
    bordercolor="firebrick",
    lightcolor="#2f2f2f",
    darkcolor="#2f2f2f",
    font=label_font
)

style.map("TCombobox",
    fieldbackground=[('readonly', '#1a1a1a')],
    background=[('readonly', '#1a1a1a')],
    foreground=[('readonly', 'white')],
    arrowcolor=[('readonly', 'firebrick')]
)

tk.Label(
    root,
    text="Choose Level (1-20):",
    font=label_font,
    fg="light gray",
    bg="#2f2f2f"
).pack()

# Emojified levels with flavor (spent way too much time coming up with all these ;>)
level_options = [
    "💀 1 – Fresh Meat", "💀 2 – Greenhorn", "💀 3 – Amateur", "💀 4 – Showing Promise", "💀 5 – Skeleton Fodder",
    "⚔️ 6 – Budding Talent", "⚔️ 7 – Trained Fighter", "⚔️ 8 – Experienced", "⚔️ 9 – ", "⚔️ 10 – Elite",
    "🔥 11", "🔥 12", "🔥 13 – Rising Legend", "🔥 14", "🔥 15",
    "🐉 16", "🐉 17", "🐉 18 – Dragon-Blooded", "🐉 19 – Legendary", "🐉 20 – Mythic"
]

level_var = tk.StringVar(value=level_options[0])
level_dropdown = ttk.Combobox(root, textvariable=level_var, values=level_options, state="readonly", font=label_font)
level_dropdown.pack(pady=5)

# Button
tk.Button(
    root,
    text="🔮 Create Character",
    command=fetch_and_display_weather,
    bg="midnight blue",
    fg="#36454F",
    font=label_font
).pack(pady=15)

# Output display
output_label = tk.Label(
    root,
    text="",
    justify="left",
    fg="ghost white",
    bg="#2f2f2f",
    font=("Georgia", 14),
    wraplength=500
)
output_label.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()

