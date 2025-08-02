import csv
import random
import os
from dotenv import load_dotenv

# Fix matplotlib import and backend setup
import matplotlib
matplotlib.use('TkAgg')  # Set backend before importing pyplot

import tkinter as tk
from tkinter import messagebox

# Add error handling for custom imports
try:
    from gui.input_form import InputForm   
    from gui.results_display import CharacterResultsFrame
    from features.character_generator import generate_character
    from features.weather_fetcher import get_weather_data_for_city, get_random_city
except ImportError as e:
    print(f"[Import Error] Failed to import required modules: {e}")
    print("Please ensure all required files are in the correct directories.")
    exit(1)

# Load environment variables
try:
    load_dotenv()
    print("Environment variables loaded successfully")
except Exception as e:
    print(f"[Environment Error] {e}")

# --- Custom GUI Theme ---
style = tk.Style()
style.theme_use("default")

# --- Helper: Get Inspirational Quote ---
def get_random_quote():
    try:
        quotes_path = os.path.join("utils", "weather_quotes.csv")
        if not os.path.exists(quotes_path):
            print(f"[Quote Warning] File not found: {quotes_path}")
            return "Forge ahead – every storm makes a stronger hero."
            
        with open(quotes_path, newline='', encoding='utf-8') as csvfile:
            quotes = [row[0] for row in csv.reader(csvfile) if row and len(row) > 0]
        return random.choice(quotes) if quotes else "Forge ahead – every storm makes a stronger hero."
    except Exception as e:
        print(f"[Quote Error] {e}")
        return "Forge ahead – every storm makes a stronger hero."

# --- App Setup ---
def create_main_window():
    root = tk.Tk()
    root.title("Tempestbourne: Weather-Forged Adventurers")
    
    # Set minimum window size
    root.minsize(800, 600)
    
    return root

# Initialize the main window
root = create_main_window()

# Container for form and buttons
main_container = tk.Frame(root)
main_container.pack(padx=20, pady=20, fill="both", expand=True)

# --- Inspirational Quote ---
quote_var = tk.StringVar(value=get_random_quote())
quote_label = tk.Label(
    main_container,
    textvariable=quote_var,
    wraplength=500,
    justify="center",
    font=("Helvetica", 10, "italic")
)
quote_label.pack(pady=(0, 10))

# Scrollable results container
results_container_frame = tk.Frame(main_container)
results_container_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(results_container_frame)
scrollbar = tk.Scrollbar(results_container_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Bind mouse wheel for scrolling
def _on_mousewheel(event):
    try:
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    except:
        # Fallback for different platforms
        canvas.yview_scroll(-1 if event.delta > 0 else 1, "units")

# Bind mousewheel to canvas instead of scrollable_frame
canvas.bind_all("<MouseWheel>", _on_mousewheel)

# --- Form Submission Handler ---
def handle_form_submission(form_data):
    try:
        city = form_data["city"]
        date = form_data["date"]
        time = form_data["time"]
        gender = form_data["gender"]
        level = int(form_data["level"])
        requested_datetime = f"{date} {time}"

        print(f"Processing request for {city} at {requested_datetime}")

        # Get weather data
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

        # Generate characters
        char_user = generate_character(weather_user, level, gender)
        char_random = generate_character(weather_random, level, gender)

        # Clear old results
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        # Apply weather theme
        def apply_weather_theme(condition):
            if not isinstance(condition, str):
                return
                
            condition = condition.lower()

            if "rain" in condition:
                style.configure("TFrame", background="#dce3f0")
                style.configure("TLabel", background="#dce3f0")
            elif "clear" in condition:
                style.configure("TFrame", background="#fff9e6")
                style.configure("TLabel", background="#fff9e6")
            elif "cloud" in condition:
                style.configure("TFrame", background="#e6e6e6")
                style.configure("TLabel", background="#e6e6e6")
            elif "storm" in condition or "thunderstorm" in condition:
                style.configure("TFrame", background="#aa81b2")
                style.configure("TLabel", background="#aa81b2")
            elif "snow" in condition:
                style.configure("TFrame", background="#84D2F9")
                style.configure("TLabel", background="#84D2F9")
            else:
                style.configure("TFrame", background="#f5f5f5")
                style.configure("TLabel", background="#f5f5f5")

        # Get main weather condition and apply theme
        main_condition = ""
        if weather_user.get("weather") and len(weather_user["weather"]) > 0:
            main_condition = weather_user["weather"][0].get("main", "")
        apply_weather_theme(main_condition)


        # Display results
        tk.Label(scrollable_frame, text=f"🌆 {city} Adventurer", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
        CharacterResultsFrame(scrollable_frame, character=char_user).pack(pady=10)

        tk.Label(scrollable_frame, text=f"🧭 Random City: {random_city}", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
        CharacterResultsFrame(scrollable_frame, character=char_random).pack(pady=10)

        # Update quote
        quote_var.set(get_random_quote())
        
        print("Character generation completed successfully")

    except Exception as e:
        print(f"[Form Submission Error] {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

# --- Reset Handler ---
def reset_app():
    try:
        form.reset()
        quote_var.set(get_random_quote())
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        print("App reset successfully")
    except Exception as e:
        print(f"[Reset Error] {e}")

# --- Form UI ---
try:
    form = InputForm(main_container, on_submit_callback=handle_form_submission)
    form.pack(pady=(0, 10))
except Exception as e:
    print(f"[Form Creation Error] {e}")
    messagebox.showerror("Initialization Error", f"Failed to create form: {e}")
    root.destroy()
    exit(1)

# --- Buttons ---
button_frame = tk.Frame(main_container)
button_frame.pack(pady=(0, 10))

generate_btn = tk.Button(
    button_frame, 
    text="Generate Character", 
    command=lambda: handle_form_submission(form.get_form_data())
)
# generate_btn.grid(row=0, column=0, padx=5)

reset_btn = tk.Button(button_frame, text="Reset", command=reset_app)
reset_btn.grid(row=0, column=1, padx=5)

# --- Bind Return Key ---
root.bind("<Return>", lambda event: handle_form_submission(form.get_form_data()))

# Base styling
base_bg = "#f5f5f5"
accent_color = "#6a5acd"
highlight_color = "#ffcc00"

style.configure("TFrame", background=base_bg)
style.configure("TLabel", background=base_bg, font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10, "bold"), padding=6)
style.configure("TScrollbar", troughcolor=accent_color, background=highlight_color)
style.map("TScrollbar", background=[("active", highlight_color)])

quote_label.configure(foreground="#333333")

print("App setup completed successfully")
print("Starting main event loop...")

# --- Run App ---
if __name__ == "__main__":
    try:
        print("Launching Tempestbourne application...")
        root.mainloop()
    except KeyboardInterrupt:
        print("Application interrupted by user")
    except Exception as e:
        print(f"[Main Error] {e}")
        messagebox.showerror("Critical Error", f"Application crashed: {e}")
    finally:
        print("Application shutting down...")