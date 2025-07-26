# Input Form
# gui/input_form.py

import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class InputForm(ttk.Frame):
    def __init__(self, parent, on_submit_callback):
        super().__init__(parent)
        self.on_submit_callback = on_submit_callback
        self.build_form()

    def build_form(self):
        # --- City Input ---
        ttk.Label(self, text="City:").grid(row=0, column=0, sticky="w", pady=(5, 2))
        self.city_entry = ttk.Entry(self)
        self.city_entry.grid(row=0, column=1, pady=(5, 2))

        # --- Date Dropdown (Next 4 days) ---
        ttk.Label(self, text="Date:").grid(row=1, column=0, sticky="w", pady=2)
        today = datetime.now()
        self.date_options = [
            (today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(4)
        ]
        self.date_var = tk.StringVar(value=self.date_options[0])
        self.date_menu = ttk.OptionMenu(self, self.date_var, self.date_options[0], *self.date_options)
        self.date_menu.grid(row=1, column=1, pady=2)

        # --- Time Input (HH:MM 24h) ---
        ttk.Label(self, text="Time (24h - HH:MM):").grid(row=2, column=0, sticky="w", pady=2)
        self.time_entry = ttk.Entry(self)
        self.time_entry.insert(0, "17:00")
        self.time_entry.grid(row=2, column=1, pady=2)

        # --- Gender Dropdown ---
        ttk.Label(self, text="Gender:").grid(row=3, column=0, sticky="w", pady=2)
        self.gender_var = tk.StringVar(value="Female")
        gender_options = ["Male", "Female", "Nonbinary"]
        self.gender_menu = ttk.OptionMenu(self, self.gender_var, gender_options[1], *gender_options)
        self.gender_menu.grid(row=3, column=1, pady=2)

        # --- Level Dropdown (1–20) ---
        ttk.Label(self, text="Level:").grid(row=4, column=0, sticky="w", pady=2)
        self.level_var = tk.IntVar(value=1)
        level_options = list(range(1, 21))
        self.level_menu = ttk.OptionMenu(self, self.level_var, level_options[0], *level_options)
        self.level_menu.grid(row=4, column=1, pady=2)

        # --- Submit Button ---
        submit_btn = ttk.Button(self, text="Generate Character", command=self.submit)
        submit_btn.grid(row=5, column=0, columnspan=2, pady=(10, 5))

    def submit(self):
        form_data = {
            "city": self.city_entry.get(),
            "date": self.date_var.get(),
            "time": self.time_entry.get(),
            "gender": self.gender_var.get(),
            "level": self.level_var.get()
        }
        self.on_submit_callback(form_data)

