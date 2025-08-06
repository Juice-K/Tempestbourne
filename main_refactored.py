import csv
import random
import os
from dotenv import load_dotenv
 
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog

# Added error handling for custom imports
try:
    from gui.input_form import InputForm
    from gui.results_display import CharacterResultsFrame
    from features.character_generator import generate_character
    from features.weather_fetcher import get_weather_data_for_city, get_random_city
    from features.export_tools import export_character_to_pdf # Import the export "download all" function
except ImportError as e:
    exit(1)
    
# Load environment variables
try:
    load_dotenv()
except Exception as e:
    
# --- Custom GUI Theme ---
style = ttk.Style()
style.theme_use("default")

# Base styling
base_bg = "#F5F5F5"
accent_color = "#6A5ACD"
highlight_color = "#FFCC00"
style.configure("TFrame", background=base_bg)
style.configure("TLabel", background=base_bg, font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10, "bold"), padding=6)
style.configure("TScrollbar", troughcolor=accent_color, background=highlight_color)
style.map("TScrollbar", background=[("active", highlight_color)])


# --- Get Inspirational Quote ---
def get_random_quote():
    try:
        quotes_path = os.path.join("utils", "weather_quotes.csv")
        if not os.path.exists(quotes_path):
            return "Forge ahead – every storm makes a stronger hero."
        with open(quotes_path, newline='', encoding='utf-8') as csvfile:
            quotes = [row[0] for row in csv.reader(csvfile) if row and len(row) > 0])
        return random.choice(quotes) if quotes else "Forge ahead – every storm makes a stronger hero."
    except Exception as e:
        return "Forge ahead – every storm makes a stronger hero."
    
# --- App Setup ---
def create_main_window():
    root = tk.Tk()
    root.title("Tempestbourne: Weather-Forged Adventurers")
    # Set minimum window size
    root.minsize(1200, 800)
    return root

# Initialize the main window
root = create_main_window()

# Container for form and buttons
main_container = ttk.Frame(root)
main_container.pack(padx=40, pady=40, fill="both", expand=True)

# --- Form Submission Handler ---
def handle_form_submission(form_data):
    global latest_char_user, latest_char_random
    try:
        city = form_data["city"]
        date = form_data["date"]
        time = form_data["time"]
        gender = form_data["gender"]
        level = int(form_data["level"])
        requested_datetime = f"{date} {time}"
        
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
            return
        
        # Generate characters
        latest_char_user = generate_character(weather_user, level, gender)
        latest_char_random = generate_character(weather_random, level, gender)
        
        # Clear old results
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
            
        # Apply weather theme
        def apply_weather_theme(condition):
            if not isinstance(condition, str):
                return
            condition = condition.lower()
            if "rain" in condition:
                style.configure("TFrame", background="#DCE3F0")
                style.configure("TLabel", background="#DCE3F0")
            elif "clear" in condition:
                style.configure("TFrame", background="#FFF9E6")
                style.configure("TLabel", background="#FFF9E6")
            elif "cloud" in condition:
                style.configure("TFrame", background="#E6E6E6")
                style.configure("TLabel", background="#E6E6E6")
            elif "storm" in condition or "thunderstorm" in condition:
                style.configure("TFrame", background="#AA81B2")
                style.configure("TLabel", background="#AA81B2")
            elif "snow" in condition:
                style.configure("TFrame", background="#84D2F9")
                style.configure("TLabel", background="#84D2F9")
            else:
                style.configure("TFrame", background="#F5F5F5")
                style.configure("TLabel", background="#F5F5F5")
                
        # Get main weather condition and apply theme
        main_condition = ""
        if weather_user.get("weather") and len(weather_user["weather"]) > 0:
            main_condition = weather_user["weather"][0].get("main", "")
        apply_weather_theme(main_condition)

        # --- Export Both Button ---
        def export_both_characters():
            if not latest_char_user or not latest_char_random:
                messagebox.showerror("Export Error", "No characters to export.")
                return

            folder_path = filedialog.askdirectory(title="Choose Folder to Save PDFs")
            if folder_path:
                try:
                    export_character_to_pdf(
                        character_to_dict(latest_char_user),
                        filename=os.path.join(folder_path, f"{latest_char_user.name}.pdf")
                    )
                    export_character_to_pdf(
                        character_to_dict(latest_char_random),
                        filename=os.path.join(folder_path, f"{latest_char_random.name}.pdf")
                    )
                    messagebox.showinfo("Export Successful", f"Both characters saved in:\n{folder_path}")
                except Exception as e:
                    messagebox.showerror("Export Failed", f"Could not save PDFs:\n{e}")

        # Button to export both
        ttk.Button(
            scrollable_frame,
            text="Download Both Characters",
            command=export_both_characters
        ).pack(pady=(5, 15))
        
        # Display results
        ttk.Label(scrollable_frame, text=f":city_sunset: {city} Adventurer", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
        CharacterResultsFrame(scrollable_frame, character=latest_char_user).pack(pady=10)
        ttk.Label(scrollable_frame, text=f":compass: Random City: {random_city}", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
        CharacterResultsFrame(scrollable_frame, character=latest_char_random).pack(pady=10)
        
        # Update quote
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        

# --- Form UI ---
try:
    form = InputForm(main_container, on_submit_callback=handle_form_submission)
    form.pack(pady=(0, 10))
except Exception as e:
    messagebox.showerror("Initialization Error", f"Failed to create form: {e}")
    root.destroy()
    exit(1)
    
# --- Reset Handler ---
def reset_app():
    try:
        form.reset()
        quote_var.set(get_random_quote())
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
    except Exception as e:
            
    
# --- Buttons ---
button_frame = ttk.Frame(main_container)
button_frame.pack(pady=(0, 10))
generate_btn = ttk.Button(
    button_frame,
    text="Generate Character",
    command=lambda: handle_form_submission(form.get_form_data())
)
reset_btn = ttk.Button(button_frame, text="Reset", command=reset_app)
reset_btn.grid(row=0, column=1, padx=5)

# --- Inspirational Quote Frame ---
quote_frame = ttk.Frame(main_container)
quote_frame.pack(side="top", fill="x", pady=(0, 15))

quote_var = tk.StringVar(value=get_random_quote())
quote_label = ttk.Label(
    quote_frame,
    textvariable=quote_var,
    wraplength=800,
    justify="center",
    font=("Helvetica", 16, "italic"),
    foreground="blue"
)
quote_label.pack(anchor="center")) # Make sure it's always visible and at the top 

# Scrollable results container
results_container_frame = ttk.Frame(main_container)
results_container_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(results_container_frame)
scrollbar = ttk.Scrollbar(results_container_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

# Ensure scrollable frame expands with window
def resize_inner_frame(event):
    canvas.itemconfig(inner_window, width=event.width) # Adjust width to match canvas 
    
inner_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.bind("<Configure>", resize_inner_frame)
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

# --- Global to hold latest characters ---
latest_char_user = None
latest_char_random = None


def character_to_dict(character):
    """
    Converts a character object into a dictionary for export.
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
    



# --- Bind Return Key ---
root.bind("<Return>", lambda event: handle_form_submission(form.get_form_data()))


# --- Run App ---
if __name__ == "__main__":
    try:
        root.mainloop()
    except KeyboardInterrupt:
    except Exception as e:
        messagebox.showerror("Critical Error", f"Application crashed: {e}")
    finally: 