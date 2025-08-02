# import pandas as pd
# import eyed3

# # Load the CSV file
# df = pd.read_csv("your_music_data.csv")

# # Iterate through the rows
# for index, row in df.iterrows():
#     file_path = row['filepath']  # Or wherever your file path is stored
#     try:
#         audio_file = eyed3.load(file_path)
#         if audio_file is not None:
#             # Access metadata
#             title = audio_file.tag.title
#             artist = audio_file.tag.artist
#             album = audio_file.tag.album

#             # Do something with the metadata, like printing or writing to another CSV
#             print(f"Title: {title}, Artist: {artist}, Album: {album}")

#             # Example of updating the dataframe with metadata
#             df.loc[index, 'title'] = title
#             df.loc[index, 'artist'] = artist
#             df.loc[index, 'album'] = album

#     except Exception as e:
#         print(f"Error processing {file_path}: {e}")

# # Optionally, save the updated dataframe to a new CSV
# df.to_csv("updated_music_data.csv", index=False)

# # All the above is specifically for mp3s

# # main.py
# version 1

# # --- Custom GUI Theme ---
# style = ttk.Style() # Use default theme
# style.theme_use("default") # Set the default theme


# # --- Helper: Get Inspirational Quote ---
# def get_random_quote():
#     try:
#         with open(os.path.join("utils", "weather_quotes.csv"), newline='') as csvfile:
#             quotes = [row[0] for row in csv.reader(csvfile) if row]
#         return random.choice(quotes) if quotes else ""
#     except Exception as e:
#         print(f"[Quote Error] {e}")
#         return "Forge ahead – every storm makes a stronger hero."

# # --- App Setup ---
# root = tk.Tk()
# root.title("Tempestbourne: Weather-Forged Adventurers")

# # Container for form and buttons
# main_container = ttk.Frame(root)
# main_container.pack(padx=20, pady=20, fill="both", expand=True)

# # --- Inspirational Quote ---
# quote_var = tk.StringVar(value=get_random_quote())
# quote_label = ttk.Label(
#     main_container,
#     textvariable=quote_var,
#     wraplength=500,
#     justify="center",
#     font=("Helvetica", 10, "italic")
# )
# quote_label.pack(pady=(0, 10))

# # Scrollable results container
# results_container_frame = ttk.Frame(main_container)
# results_container_frame.pack(fill="both", expand=True)

# canvas = tk.Canvas(results_container_frame)
# scrollbar = ttk.Scrollbar(results_container_frame, orient="vertical", command=canvas.yview)
# scrollable_frame = ttk.Frame(canvas)

# scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# canvas.configure(yscrollcommand=scrollbar.set)

# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")

# # Bind mouse wheel for scrolling
# def _on_mousewheel(event):
#     canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# scrollable_frame.bind_all("<MouseWheel>", _on_mousewheel)


# # --- Form Submission Handler ---
# def handle_form_submission(form_data):
#     city = form_data["city"]
#     date = form_data["date"]
#     time = form_data["time"]
#     gender = form_data["gender"]
#     level = int(form_data["level"])
#     requested_datetime = f"{date} {time}"

#     try:
#         weather_user = get_weather_data_for_city(city, requested_datetime)
#     except Exception as e:
#         messagebox.showerror("Weather Error", f"Could not fetch weather for {city}.\n{e}")
#         return

#     random_city = get_random_city(exclude=city)
#     try:
#         weather_random = get_weather_data_for_city(random_city, requested_datetime)
#     except Exception as e:
#         print(f"[Weather Error] Failed to fetch weather for random city: {e}")
#         return

#     # 🎲 Generate characters
#     char_user = generate_character(weather_user, level, gender)
#     char_random = generate_character(weather_random, level, gender)

#     # 🧹 Clear old results
#     for widget in scrollable_frame.winfo_children():
#         widget.destroy()

#     # 🖼️ Display weather comparison    
#     ttk.Label(scrollable_frame, text="🌍 Weather Comparison", font=("Helvetica", 12, "bold")).pack(pady=(20, 0))
#     WeatherComparisonFrame(
#         scrollable_frame,
#         weather1=weather_user,
#         weather2=weather_random,
#         city1=city,
#         city2=random_city
#     ).pack(pady=10, fill="both", expand=True)


#     # alter theme by weather results
#     def apply_weather_theme(condition):
#         if not isinstance(condition, str):  # Ensure condition is a string
#             return  # or log it and return  

#         condition = condition.lower()  # Normalize condition to lowercase to avoid crashes

#         if "rain" in condition:
#             style.configure("TFrame", background="#dce3f0") # Light blue for rainy weather
#             style.configure("TLabel", background="#dce3f0")
#         elif "clear" in condition:
#             style.configure("TFrame", background="#fff9e6") # Light cream for clear weather
#             style.configure("TLabel", background="#fff9e6")
#         elif "cloud" in condition:
#             style.configure("TFrame", background="#e6e6e6") # Light gray for cloudy weather
#             style.configure("TLabel", background="#e6e6e6")
#         elif "storm" in condition:
#             style.configure("TFrame", background="#f0f0f07f") # Light gray for stormy weather
#             style.configure("TLabel", background="#f0f0f07f")
#         elif "snow" in condition:
#             style.configure("TFrame", background="#84D2F9") # Light blue for snowy weather
#             style.configure("TLabel", background="#84D2F9")
#         elif "thunderstorm" in condition:
#             style.configure("TFrame", background="#aa81b2") # Dark purple for stormy weather
#             style.configure("TLabel", background="#5e0770")
#         else:
#             style.configure("TFrame", background="#f5f5f5") # light gray background
#             style.configure("TLabel", background="#f5f5f5")

#     main_condition = weather_user.get("weather", [{}])[0].get("main", "") # Get the main weather condition
#     apply_weather_theme(main_condition)                                   # Apply the theme based on the main condition

#     # 🖼️ Display results in a scrollbox
#     ttk.Label(scrollable_frame, text=f"🌆 {city} Adventurer", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
#     CharacterResultsFrame(scrollable_frame, character=char_user).pack(pady=10)

#     ttk.Label(scrollable_frame, text=f"🧭 Random City: {random_city}", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
#     CharacterResultsFrame(scrollable_frame, character=char_random).pack(pady=10)

#     # 🌟 Update quote
#     quote_var.set(get_random_quote())

# # --- Reset Handler ---
# def reset_app():
#     form.reset()
#     quote_var.set(get_random_quote())
#     for widget in scrollable_frame.winfo_children():
#         widget.destroy()

# # --- Form UI ---
# form = InputForm(main_container, on_submit_callback=handle_form_submission)
# form.pack(pady=(0, 10))

# # --- Buttons ---
# button_frame = ttk.Frame(main_container)
# button_frame.pack(pady=(0, 10))

# generate_btn = ttk.Button(button_frame, text="Generate Character", command=lambda: handle_form_submission(form.get_form_data()))

# reset_btn = ttk.Button(button_frame, text="Reset", command=reset_app)
# reset_btn.grid(row=0, column=1, padx=5)

# # --- Bind Return Key ---
# root.bind("<Return>", lambda event: handle_form_submission(form.get_form_data()))


# # Base colors
# base_bg = "#f5f5f5"
# accent_color = "#6a5acd"  # Slate blue
# highlight_color = "#ffcc00"  # Gold

# # General styling
# style.configure("TFrame", background=base_bg)
# style.configure("TLabel", background=base_bg, font=("Helvetica", 10))
# style.configure("TButton", font=("Helvetica", 10, "bold"), padding=6)
# style.configure("TScrollbar", troughcolor=accent_color, background=highlight_color)

# # Scrollbar active hover
# style.map("TScrollbar", background=[("active", highlight_color)])

# # Quote tweak
# quote_label.configure(foreground="#333333")

# # ensure the code is getting to this point
# print("App launching...")

# # --- Run App ---
# if __name__ == "__main__":
#     try:
#         root.mainloop()
#     except Exception as e:
#         print(f"[Main Error] {e}")
        
        
        
#         # after Bolt and additional print statemenets
        

# Add error handling for custom imports
try:
    from gui.input_form import InputForm   
    from gui.results_display import CharacterResultsFrame, WeatherComparisonFrame
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
style = ttk.Style()
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
main_container = ttk.Frame(root)
main_container.pack(padx=20, pady=20, fill="both", expand=True)

# --- Inspirational Quote ---
quote_var = tk.StringVar(value=get_random_quote())
quote_label = ttk.Label(
    main_container,
    textvariable=quote_var,
    wraplength=500,
    justify="center",
    font=("Helvetica", 10, "italic")
)
quote_label.pack(pady=(0, 10))

# Scrollable results container
results_container_frame = ttk.Frame(main_container)
results_container_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(results_container_frame)
scrollbar = ttk.Scrollbar(results_container_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

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

        # Display weather comparison    
        ttk.Label(scrollable_frame, text="🌍 Weather Comparison", font=("Helvetica", 12, "bold")).pack(pady=(20, 0))
        WeatherComparisonFrame(
            scrollable_frame,
            weather1=weather_user,
            weather2=weather_random,
            city1=city,
            city2=random_city
        ).pack(pady=10, fill="both", expand=True)

        # Display results
        ttk.Label(scrollable_frame, text=f"🌆 {city} Adventurer", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
        CharacterResultsFrame(scrollable_frame, character=char_user).pack(pady=10)

        ttk.Label(scrollable_frame, text=f"🧭 Random City: {random_city}", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
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
button_frame = ttk.Frame(main_container)
button_frame.pack(pady=(0, 10))

generate_btn = ttk.Button(
    button_frame, 
    text="Generate Character", 
    command=lambda: handle_form_submission(form.get_form_data())
)

reset_btn = ttk.Button(button_frame, text="Reset", command=reset_app)
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

  

#     # --- Weather Comparison Plots ---
#     if city1 and weather1 and city2 and weather2:
#         self.plot_ridgeline(scroll_frame)
#         self.plot_radial(scroll_frame)      
        
#  # DnD-styled theme for the plots
# sns.set_theme(style="white", context="notebook")
# sns.set_palette(["#7B3F00", "#2E8B57"])  # deep brown and forest green

# # Matplotlib configuration for a DnD aesthetic
# plt.rcParams.update({
#     "axes.facecolor": "#fdf6e3",
#     "figure.facecolor": "#f5f0dc",
#     "axes.edgecolor": "#5a4b3b",
#     "axes.labelcolor": "#2e2a1c",
#     "text.color": "#2e2a1c",
#     "xtick.color": "#5a4b3b",
#     "ytick.color": "#5a4b3b",
#     "axes.titleweight": "bold",
#     "font.family": "serif",
#     "font.serif": ["Georgia", "Palatino Linotype", "Book Antiqua"]
# })
       
#         # WeatherComparisonFrame creates a tabbed interface for weather comparisons
# class WeatherComparisonFrame(tk.Notebook):

#     # Initialize the WeatherComparisonFrame with weather data and cities
#     def __init__(self, parent, weather1, weather2, city1, city2):
#         super().__init__(parent)

#         self.weather_df = self.prepare_weather_dataframe(weather1, weather2, city1, city2)

#         self.ridgeline_tab = tk.Frame(self)
#         self.radial_tab = tk.Frame(self)

#         self.add(self.ridgeline_tab, text="Ridgeline")
#         self.add(self.radial_tab, text="Radial")

#         self.plot_ridgeline(self.ridgeline_tab)
#         self.plot_radial(self.radial_tab)

#     # Prepare weather data for plotting
#     def prepare_weather_dataframe(self, weather1, weather2, city1, city2):
#         # Normalize the dictionaries in each list
#         df1 = pd.json_normalize(weather1)
#         df1["city"] = city1

#         df2 = pd.json_normalize(weather2)
#         df2["city"] = city2

#         combined_df = pd.concat([df1, df2], ignore_index=True)
#         return combined_df
    
#     # Ridgeline plot for weather comparison
#     def plot_ridgeline(self, tab):
#         fig, ax = plt.subplots(figsize=(7, 5))
#         try:
#             sns.violinplot(
#                 data=self.weather_df,
#                 x="temperature",
#                 y="city",
#                 scale="width",
#                 inner="quartile",
#                 ax=ax
#             )
#             ax.set_title("Weather Clash of Realms", fontsize=14, fontweight="bold", color="#5a0f0f")
#             ax.set_xlabel("Temperature (°C)")
#             ax.set_ylabel("City")
#         except Exception as e:
#             ax.text(0.5, 0.5, f"Plot Error: {e}", ha='center')

#         canvas = FigureCanvasTkAgg(fig, master=tab)
#         canvas.draw()
#         canvas.get_tk_widget().pack(fill="both", expand=True)
        
#     # Radial plot for weather comparison
#     def plot_radial(self, tab):
#         fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
#         try:
#             summary = self.weather_df.groupby('city')[['temperature', 'humidity', 'wind_speed']].mean()
#             categories = list(summary.columns)
#             cities = summary.index
#             num_vars = len(categories)
#             angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
#             angles += angles[:1]  # close the circle

#             for city in cities:
#                 values = summary.loc[city].tolist()
#                 values += values[:1]
#                 ax.plot(angles, values, label=city, linewidth=2)
#                 ax.fill(angles, values, alpha=0.25)

#             ax.set_title("Mystic Elements Chart", fontsize=14, fontweight="bold", color="#5a0f0f")
#             ax.set_xticks(angles[:-1])
#             ax.set_xticklabels(categories, fontsize=10, fontweight="bold")
#             ax.tick_params(colors="#5a4b3b")
#             ax.grid(color="#8b7765")
#             ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
#         except Exception as e:
#             ax.text(0.5, 0.5, f"Plot Error: {e}", ha='center')

#         canvas = FigureCanvasTkAgg(fig, master=tab)
#         canvas.draw()
#         canvas.get_tk_widget().pack(fill="both", expand=True)

