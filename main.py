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

def fetch_and_display_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city.")
        return

    try:
        data = get_current_weather(city)
        save_weather_data(city, data)

        result = f"City: {data['name']}\n"
        result += f"Condition: {data['weather'][0]['description']}\n"
        result += f"Temp: {data['main']['temp']}°C\n"
        result += f"Humidity: {data['main']['humidity']}%\n"
        result += f"Wind: {data['wind']['speed']} m/s\n"
        output_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("TEMPESTBOURNE Characater Generator", tkFont.Font(family="Gothic", size=24, weight="bold", color="midnightred"))
root.geometry("550x350")

tk.Label(root, text="Enter City:").pack(pady=(10, 0))
city_entry = tk.Entry(root, width=30)
city_entry.pack()

tk.Label(root, integer="Choose Level (1-20):").pack(pady=(10, 0))
city_entry = tk.Entry(root, width=30)
city_entry.pack()

tk.Button(root, text="Create Characters", command=fetch_and_display_weather).pack(pady=10)

output_label = tk.Label(root, text="", justify="left")
output_label.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
