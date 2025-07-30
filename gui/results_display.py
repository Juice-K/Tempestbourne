# Results Display
# gui/results_display.py

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import numpy as np
import pandas as pd

class CharacterResultsFrame(tk.Frame):
    def __init__(self, parent, character, city1=None, weather1=None, city2=None, weather2=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.character = character
        self.city1 = city1
        self.weather1 = weather1
        self.city2 = city2
        self.weather2 = weather2

        # --- Create canvas + scrollbar ---
        canvas = tk.Canvas(self, borderwidth=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- Header ---
        header = ttk.Label(scroll_frame, text=f"{character.name} — Level {character.level} {character.race} {character.char_class}", font=("Helvetica", 14, "bold"))
        header.pack(pady=(10, 5))

        # --- Bio ---
        bio_label = ttk.Label(scroll_frame, text=character.bio, wraplength=400, justify="center")
        bio_label.pack(pady=(0, 10))

        # --- Stats ---
        stats_frame = ttk.LabelFrame(scroll_frame, text="Stats")
        stats_frame.pack(padx=10, pady=5, fill="x")
        for stat, value in character.stats.items():
            ttk.Label(stats_frame, text=f"{stat}: {value}").pack(anchor="w", padx=10)

        # --- Skills ---
        skills_frame = ttk.LabelFrame(scroll_frame, text="Skills")
        skills_frame.pack(padx=10, pady=5, fill="x")
        for skill in character.skills:
            ttk.Label(skills_frame, text=skill).pack(anchor="w", padx=10)

        # --- Equipment ---
        equip_frame = ttk.LabelFrame(scroll_frame, text="Equipment")
        equip_frame.pack(padx=10, pady=5, fill="x")
        for item in character.equipment:
            ttk.Label(equip_frame, text=item).pack(anchor="w", padx=10)

        # --- Alignment Display ---
        align_label = ttk.Label(scroll_frame, text=f"Alignment: {character.alignment}", font=("Helvetica", 10, "italic"))
        align_label.pack(pady=(5, 10))

        # --- Weather Comparison Plots ---
        if city1 and weather1 and city2 and weather2:
            self.plot_ridgeline(scroll_frame)
            self.plot_radial(scroll_frame)



# DnD-styled theme for the plots
sns.set_theme(style="white", context="notebook")
sns.set_palette(["#7B3F00", "#2E8B57"])  # deep brown and forest green

# Matplotlib configuration for a DnD aesthetic
plt.rcParams.update({
    "axes.facecolor": "#fdf6e3",
    "figure.facecolor": "#f5f0dc",
    "axes.edgecolor": "#5a4b3b",
    "axes.labelcolor": "#2e2a1c",
    "text.color": "#2e2a1c",
    "xtick.color": "#5a4b3b",
    "ytick.color": "#5a4b3b",
    "axes.titleweight": "bold",
    "font.family": "serif",
    "font.serif": ["Georgia", "Palatino Linotype", "Book Antiqua"]
})

# WeatherComparisonFrame creates a tabbed interface for weather comparisons
class WeatherComparisonFrame(ttk.Notebook):

    # Initialize the WeatherComparisonFrame with weather data and cities
    def __init__(self, parent, weather1, weather2, city1, city2):
        super().__init__(parent)

        self.weather_df = self.prepare_weather_dataframe(weather1, weather2, city1, city2)

        self.ridgeline_tab = ttk.Frame(self)
        self.radial_tab = ttk.Frame(self)

        self.add(self.ridgeline_tab, text="Ridgeline")
        self.add(self.radial_tab, text="Radial")

        self.plot_ridgeline(self.ridgeline_tab)
        self.plot_radial(self.radial_tab)

    # Prepare weather data for plotting
    def prepare_weather_dataframe(self, weather1, weather2, city1, city2):
        # Normalize the dictionaries in each list
        df1 = pd.json_normalize(weather1)
        df1["city"] = city1

        df2 = pd.json_normalize(weather2)
        df2["city"] = city2

        combined_df = pd.concat([df1, df2], ignore_index=True)
        return combined_df
    
    # Ridgeline plot for weather comparison
    def plot_ridgeline(self, tab):
        fig, ax = plt.subplots(figsize=(7, 5))
        try:
            sns.violinplot(
                data=self.weather_df,
                x="temperature",
                y="city",
                scale="width",
                inner="quartile",
                ax=ax
            )
            ax.set_title("Weather Clash of Realms", fontsize=14, fontweight="bold", color="#5a0f0f")
            ax.set_xlabel("Temperature (°C)")
            ax.set_ylabel("City")
        except Exception as e:
            ax.text(0.5, 0.5, f"Plot Error: {e}", ha='center')

        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
    # Radial plot for weather comparison
    def plot_radial(self, tab):
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
        try:
            summary = self.weather_df.groupby('city')[['temperature', 'humidity', 'wind_speed']].mean()
            categories = list(summary.columns)
            cities = summary.index
            num_vars = len(categories)
            angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
            angles += angles[:1]  # close the circle

            for city in cities:
                values = summary.loc[city].tolist()
                values += values[:1]
                ax.plot(angles, values, label=city, linewidth=2)
                ax.fill(angles, values, alpha=0.25)

            ax.set_title("Mystic Elements Chart", fontsize=14, fontweight="bold", color="#5a0f0f")
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(categories, fontsize=10, fontweight="bold")
            ax.tick_params(colors="#5a4b3b")
            ax.grid(color="#8b7765")
            ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
        except Exception as e:
            ax.text(0.5, 0.5, f"Plot Error: {e}", ha='center')

        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)



# option stats frame
# row = 0
# for i, (stat, value) in enumerate(character.stats.items()):
#     ttk.Label(stats_frame, text=f"{stat}: {value}").grid(row=row, column=i % 2, sticky="w", padx=10)
#     if i % 2 == 1:
#         row += 1
