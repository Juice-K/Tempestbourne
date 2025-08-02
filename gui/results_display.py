# Results Display
# gui/results_display.py

import tkinter as tk
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
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- Header ---
        header = tk.Label(scroll_frame, text=f"{character.name} — Level {character.level} {character.race} {character.char_class}", font=("Helvetica", 14, "bold"))
        header.pack(pady=(10, 5))

        # --- Bio ---
        bio_label = tk.Label(scroll_frame, text=character.bio, wraplength=400, justify="center")
        bio_label.pack(pady=(0, 10))

        # --- Stats ---
        stats_frame = tk.LabelFrame(scroll_frame, text="Stats")
        stats_frame.pack(padx=10, pady=5, fill="x")
        for stat, value in character.stats.items():
            tk.Label(stats_frame, text=f"{stat}: {value}").pack(anchor="w", padx=10)

        # --- Skills ---
        skills_frame = tk.LabelFrame(scroll_frame, text="Skills")
        skills_frame.pack(padx=10, pady=5, fill="x")
        for skill in character.skills:
            tk.Label(skills_frame, text=skill).pack(anchor="w", padx=10)

        # --- Equipment ---
        equip_frame = tk.LabelFrame(scroll_frame, text="Equipment")
        equip_frame.pack(padx=10, pady=5, fill="x")
        for item in character.equipment:
            tk.Label(equip_frame, text=item).pack(anchor="w", padx=10)

        # --- Alignment Display ---
        align_label = tk.Label(scroll_frame, text=f"Alignment: {character.alignment}", font=("Helvetica", 10, "italic"))
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



# option stats frame
# row = 0
# for i, (stat, value) in enumerate(character.stats.items()):
#     tk.Label(stats_frame, text=f"{stat}: {value}").grid(row=row, column=i % 2, sticky="w", padx=10)
#     if i % 2 == 1:
#         row += 1
