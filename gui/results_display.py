# Results Display
# gui/results_display.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import numpy as np
from tkinter import filedialog  # for file dialog (manage file saving)
from features.export_tools import export_character_to_pdf

class CharacterResultsFrame(tk.Frame):
    def __init__(self, parent, character, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.character = character

        # --- Create canvas + scrollbar ---
        canvas = tk.Canvas(self, borderwidth=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- Header ---
        header = ttk.Label(self, text=f"{character.name} — Level {character.level} {character.race} {character.char_class}", font=("Helvetica", 14, "bold"))
        header.pack(pady=(10, 5))

        # --- Bio ---
        bio_label = ttk.Label(self, text=character.bio, wraplength=400, justify="center")
        bio_label.pack(pady=(0, 10))

        # --- Stats ---
        stats_frame = ttk.LabelFrame(self, text="Stats")
        stats_frame.pack(padx=10, pady=5, fill="x")

        for stat, value in character.stats.items():
            ttk.Label(stats_frame, text=f"{stat}: {value}").pack(anchor="w", padx=10)

        # --- Skills ---
        skills_frame = ttk.LabelFrame(self, text="Skills")
        skills_frame.pack(padx=10, pady=5, fill="x")
        for skill in character.skills:
            ttk.Label(skills_frame, text=skill).pack(anchor="w", padx=10)

        # --- Equipment ---
        equip_frame = ttk.LabelFrame(self, text="Equipment")
        equip_frame.pack(padx=10, pady=5, fill="x")
        for item in character.equipment:
            ttk.Label(equip_frame, text=item).pack(anchor="w", padx=10)

        # --- Alignment Display ---
        align_label = ttk.Label(self, text=f"Alignment: {character.alignment}", font=("Helvetica", 10, "italic"))
        align_label.pack(pady=(5, 10))
        
        # --- Export Button ---
        def export_pdf():
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if file_path:
                export_character_to_pdf(self.character, file_path)

        ttk.Button(scroll_frame, text="📄 Export as PDF", command=export_pdf).pack(pady=(5, 10))
        
        #  Font protection/standardization 
        font=("Helvetica", 14, "bold") or ("TkDefaultFont", 14, "bold")

class WeatherComparisonFrame(tk.Frame):
    def __init__(self, parent, weather1, weather2, city1, city2, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.weather1 = weather1
        self.weather2 = weather2
        self.city1 = city1
        self.city2 = city2

        # Create tabbed display
        tabs = ttk.Notebook(self)
        tabs.pack(fill="both", expand=True)

        # Ridgeline plot tab
        ridge_tab = ttk.Frame(tabs)
        self.plot_ridgeline(ridge_tab)
        tabs.add(ridge_tab, text="Ridgeline Plot")

        # Radial chart tab
        radial_tab = ttk.Frame(tabs)
        self.plot_radial(radial_tab)
        tabs.add(radial_tab, text="Radial Bar Chart")

    def plot_ridgeline(self, container):
        sns.set_theme(style="whitegrid")

        fig, ax = plt.subplots(figsize=(6, 4))

        temp1 = self.weather1.get("temperature", 0)
        temp2 = self.weather2.get("temperature", 0)
        hum1 = self.weather1.get("humidity", 0)
        hum2 = self.weather2.get("humidity", 0)

        data = [
            {"City": self.city1, "Metric": "Temperature", "Value": temp1},
            {"City": self.city2, "Metric": "Temperature", "Value": temp2},
            {"City": self.city1, "Metric": "Humidity", "Value": hum1},
            {"City": self.city2, "Metric": "Humidity", "Value": hum2},
        ]

        data = [
            {"City": self.city1, "Metric": "Temperature", "Value": self.weather1.get("temperature", 0)},
            {"City": self.city2, "Metric": "Temperature", "Value": self.weather2.get("temperature", 0)},
            {"City": self.city1, "Metric": "Humidity", "Value": self.weather1.get("humidity", 0)},
            {"City": self.city2, "Metric": "Humidity", "Value": self.weather2.get("humidity", 0)},
            {"City": self.city1, "Metric": "Wind Speed", "Value": self.weather1.get("wind_speed", 0)},
            {"City": self.city2, "Metric": "Wind Speed", "Value": self.weather2.get("wind_speed", 0)},
        ]

        df = pd.DataFrame(data)

        sns.violinplot(
                data=df,
                x="Value",
                y="Metric",
                hue="City",
                ax=ax,
                palette="coolwarm",
                split=True
            )

        ax.set_title("Weather Comparison")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def plot_radial(self, container):
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111, polar=True)

        categories = ["Temp", "Humidity", "Wind"]
        values1 = [
            self.weather1.get("temperature", 0),
            self.weather1.get("humidity", 0),
            self.weather1.get("wind_speed", 0)
        ]
        values2 = [
            self.weather2.get("temperature", 0),
            self.weather2.get("humidity", 0),
            self.weather2.get("wind_speed", 0)
        ]

        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        values1 += values1[:1]
        values2 += values2[:1]
        angles += angles[:1]

        ax.plot(angles, values1, label=self.city1, color='blue')
        ax.fill(angles, values1, alpha=0.25, color='blue')
        ax.plot(angles, values2, label=self.city2, color='orange')
        ax.fill(angles, values2, alpha=0.25, color='orange')

        ax.set_thetagrids(np.degrees(angles[:-1]), categories)
        ax.set_title("Radial Weather Chart")
        ax.legend(loc='upper right')

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        # --- Export Button ---
        export_button = ttk.Button(self, text="Export Character to PDF", command=self.export_character)
        export_button.pack(pady=10)
        self.export_button = export_button
        self.export_button.config(command=self.export_character)
        
    def export_character(self):
        filename = f"{self.character.name}_character_sheet.pdf"
        export_character_to_pdf(self.character.__dict__, filename)
        messagebox.showinfo("Export Successful", f"Character exported as: {filename}")
        
        

## optional stats frame
# row = 0
# for i, (stat, value) in enumerate(character.stats.items()):
#     ttk.Label(stats_frame, text=f"{stat}: {value}").grid(row=row, column=i % 2, sticky="w", padx=10)
#     if i % 2 == 1:
#         row += 1
