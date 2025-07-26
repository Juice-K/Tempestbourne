# Results Display
# gui/results_display.py

import tkinter as tk
from tkinter import ttk

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
        
        #  Font protection/standardization 
        font=("Helvetica", 14, "bold") or ("TkDefaultFont", 14, "bold")


# option stats fram
# row = 0
# for i, (stat, value) in enumerate(character.stats.items()):
#     ttk.Label(stats_frame, text=f"{stat}: {value}").grid(row=row, column=i % 2, sticky="w", padx=10)
#     if i % 2 == 1:
#         row += 1
