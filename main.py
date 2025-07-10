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

# def fetch_and_display_weather():
#     city = city_entry.get()
#     if not city:
#         messagebox.showwarning("Input Error", "Please enter a city.")
#         return

#     try:
#         data = get_current_weather(city)
#         save_weather_data(city, data)

#         result = f"City: {data['name']}\n"
#         result += f"Condition: {data['weather'][0]['description']}\n"
#         result += f"Temp: {data['main']['temp']}°C\n"
#         result += f"Humidity: {data['main']['humidity']}%\n"
#         result += f"Wind: {data['wind']['speed']} m/s\n"
#         output_label.config(text=result)

#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# # GUI Setup / altered for more gothic effect
# root = tk.Tk()
# root.title("TEMPESTBOURNE Characater Generator") 
# root.geometry("600x400")
# root.configure(bg="#2f2f2f")

# title_font = tkFont.Font(family="Gothic", size=24, weight="bold")
# tk.Label(root, text="TEMPESTBOURNE Character Generator", font=title_font, fg="dark red").pack(pady=(10, 0))


# tk.Label(root, text="Enter City:").pack(pady=(10, 0))
# city_entry = tk.Entry(root, width=30)
# city_entry.pack()

# tk.Label(root, integer="Choose Level (1-20):").pack(pady=(10, 0))
# level_entry = tk.Entry(root, width=30)
# level_entry.pack()

# tk.Button(root, text="Create Characters", command=fetch_and_display_weather).pack(pady=10)

# output_label = tk.Label(root, text="", justify="left")
# output_label.pack(pady=10)

# if __name__ == "__main__":
#     root.mainloop()


def fetch_and_display_weather():
    city = city_entry.get()
    level = level_var.get()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city.")
        return

    try:
        data = get_current_weather(city)
        save_weather_data(city, data)

        result = f"🌩️ City: {data['name']}\n"
        result += f"🌫️ Condition: {data['weather'][0]['description']}\n"
        result += f"🌡️ Temp: {data['main']['temp']}°C\n"
        result += f"💧 Humidity: {data['main']['humidity']}%\n"
        result += f"💨 Wind: {data['wind']['speed']} m/s\n"
        result += f"\n🎲 Generating character for Level {level} adventurer..."
        output_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("TEMPESTBOURNE Character Generator")
root.geometry("600x400")
root.configure(bg="#2f2f2f")  # dark slate background

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

# Level dropdown
tk.Label(
    root,
    text="Choose Level (1-20):",
    font=label_font,
    fg="light gray",
    bg="#2f2f2f"
).pack()

level_var = tk.StringVar(value="1")
level_spinner = tk.Spinbox(root, from_=1, to=20, textvariable=level_var, width=5, font=label_font)
level_spinner.pack(pady=5)

# Button
tk.Button(
    root,
    text="🔮 Create Character",
    command=fetch_and_display_weather,
    bg="midnight blue",
    fg="white",
    font=label_font
).pack(pady=15)

# Output display
output_label = tk.Label(
    root,
    text="",
    justify="left",
    fg="ghost white",
    bg="#2f2f2f",
    font=("Georgia", 10),
    wraplength=500
)
output_label.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()

