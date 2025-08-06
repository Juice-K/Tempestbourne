# Results Display
# gui/results_display.py

import tkinter as tk
from tkinter import ttk
from features.export_tools import export_character_to_pdf  # Import the export function 
from tkinter import filedialog, messagebox  # Allows the user to download the character sheet




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
        
        v_scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        h_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)

        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar.pack(side="bottom", fill="x")

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
        stats_frame = tk.LabelFrame(scroll_frame, text="Stats")
        stats_frame.pack(padx=10, pady=5, fill="x")
        for stat, value in character.stats.items():
            ttk.Label(stats_frame, text=f"{stat}: {value}").pack(anchor="w", padx=10)

        # --- Skills ---
        skills_frame = tk.LabelFrame(scroll_frame, text="Skills")
        skills_frame.pack(padx=10, pady=5, fill="x")
        for skill in character.skills:
            ttk.Label(skills_frame, text=skill).pack(anchor="w", padx=10)

        # --- Equipment ---
        equip_frame = tk.LabelFrame(scroll_frame, text="Equipment")
        equip_frame.pack(padx=10, pady=5, fill="x")
        for item in character.equipment:
            ttk.Label(equip_frame, text=item).pack(anchor="w", padx=10)

        # --- Alignment Display ---
        align_label = ttk.Label(scroll_frame, text=f"Alignment: {character.alignment}", font=("Helvetica", 10, "italic"))
        align_label.pack(pady=(5, 10))
        
        # --- Export Button ---
        export_btn = ttk.Button(
            scroll_frame,
            text="Export to PDF",
            command=lambda: export_character_to_pdf(self.character_to_dict(character))
        )
        export_btn.pack(pady=(10, 5))


    def character_to_dict(self, character):
        """
        Converts the character object to a dictionary format for PDF export.
        """
        return {
            "name": character.name,
            "race": character.race,
            "char_class": character.char_class,
            "alignment": character.alignment,
            "hp": getattr(character, "hp", "N/A"),
            "skills": getattr(character, "skills", []),
            "equipment": getattr(character, "equipment", []),
            "weather": getattr(character, "weather", "Unknown"),
            "bio": getattr(character, "bio", ""),
        }

    def save_character_pdf(self, char_dict):
        """
        Prompts the user to choose where to save the PDF and calls the export function.
        """
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile=f"{char_dict.get('name', 'tempestbourne_character')}.pdf"
        )
        if file_path:
            try:
                export_character_to_pdf(char_dict, filename=file_path)
                messagebox.showinfo("Export Successful", f"Character saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Export Failed", f"Could not save PDF:\n{e}")
                
                
# option stats frame
# row = 0
# for i, (stat, value) in enumerate(character.stats.items()):
#     tk.Label(stats_frame, text=f"{stat}: {value}").grid(row=row, column=i % 2, sticky="w", padx=10)
#     if i % 2 == 1:
#         row += 1
