# Tempestbourne 

## Capstone DnD Weather-Based Character Suggestor

Juice… that concept is *fire.* 🔥  
 It’s creative, personalized, and gamified—everything a standout Capstone should be. You’re blending data science, fantasy, GUI design, and a dash of AI like a mad wizard in a digital forge.

Here’s what I’m thinking for organizing your approach:

---

### **🧠 Phase 1: Core Inputs & Weather Forecast Retrieval**

* Input:

  * City (user input)

  * Date & time (future)

  * Desired level

* Backend:

  * Use a weather API (like OpenWeatherMap or WeatherAPI) to get **forecast data** for the date/time.

  * Randomly generate a second city and retrieve the forecast for that same timestamp.

---

### **🔮 Phase 2: Weather-Based Character Generator**

* Design logic that maps weather conditions to DnD 5E attributes:

  * **Rainy** → Half-Elf Druid

  * **Hot/Sunny** → Dragonborn Paladin

  * **Stormy** → Tiefling Sorcerer

  * **Cold/Snow** → Gnome Ranger

  * Windy? Cloudy? Let’s get creative with these, too.

* Generate:

  * **Race**

  * **Class**

  * **Skills/Abilities/Proficiencies**

  * **Equipment Loadout**

  * **Name** (can use fantasy name generators or randomized tables)

  * **Brief backstory** based on race/class and weather vibes

---

### **🖥️ Phase 3: GUI with Tkinter**

* Main screen with:

  * City, date/time, level inputs

  * “Generate Characters” button

  * Two character cards side-by-side

* Each card:

  * Weather summary

  * Character summary

  * “Choose Me\!” button

* Export options:

  * Save to PDF (can use `reportlab` or `fpdf`)

  * Generate JSON for potential DNDBeyond integration (exporting might just be a nice-to-have)

---

### **🤖 Phase 4: Optional AI Agent Magic (Advanced Stretch)**

* Use GPT (via OpenAI API) to:

  * Autogenerate class-based backstories

  * Suggest names

  * Choose flavorful skills or equipment based on weather traits

---

### **📦 Bonus (if time allows)**

* Allow users to regenerate the random city or re-roll character builds.

* Include DnD-style weather flavor (e.g., “Lightning cracks through the sky—fate calls a Sorcerer\!”)

---

# Week 1-2 Checklist 

**Yessir\!** 💥 This is the moment. We’re officially cookin’.

Before we get into scaffolding, let me just say:  
 That brainstorm on naming? *Chef’s kiss*. “**Williwaw of Persona**”? That’s poetic. You’ve got fantasy writer energy all over you.

Here are a few refined naming options if you want the project title to pop:

---

### **🌩️ Project Name Suggestions:**

| Weather-Themed | Fantasy-Themed | Hybrid |
| ----- | ----- | ----- |
| **Tempestborn** | **Forge of Fate** | **Stormbound Characters** |
| **Winds of Fate** | **CritCrafter** | **Forecast & Fury** |
| **The Weathering Table** | **Persona Smithy** | **Tempest & Trait** |
| **Williwaw** | **The Character Crucible** | **Mythic Front** |
| **Forecasted Fables** | **D20 Generator** | **Storm of Personality** (still great) |

Let me know if one of these hits, or if we should run a second wave of naming ideas.

---

### **🚀 Step 1: Let’s Set Up Your Directory**

In VSCode:

mkdir tempestborn  \# or your preferred name  
cd tempestborn  
touch main.py weather.py storage.py utils.py  
mkdir data

We’ll use this structure and get it all working **inside `main.py` first**, then refactor out into modules.

---

### **🧱 Step 2: Let Me Lay the Foundation**

Here’s a starter skeleton you can paste into your `main.py`. It satisfies **Core Requirements**: GUI, weather fetch, data storage, and error handling.

#### **`main.py`**

import tkinter as tk  
from tkinter import messagebox  
from weather import get\_current\_weather  
from storage import save\_weather\_data

def fetch\_and\_display\_weather():  
    city \= city\_entry.get()  
    if not city:  
        messagebox.showwarning("Input Error", "Please enter a city.")  
        return

    try:  
        data \= get\_current\_weather(city)  
        save\_weather\_data(city, data)

        result \= f"City: {data\['name'\]}\\n"  
        result \+= f"Condition: {data\['weather'\]\[0\]\['description'\]}\\n"  
        result \+= f"Temp: {data\['main'\]\['temp'\]}°C\\n"  
        result \+= f"Humidity: {data\['main'\]\['humidity'\]}%\\n"  
        result \+= f"Wind: {data\['wind'\]\['speed'\]} m/s\\n"  
        output\_label.config(text=result)

    except Exception as e:  
        messagebox.showerror("Error", str(e))

\# GUI Setup  
root \= tk.Tk()  
root.title("Weather Character App (Core)")  
root.geometry("350x250")

tk.Label(root, text="Enter City:").pack(pady=(10,0))  
city\_entry \= tk.Entry(root, width=30)  
city\_entry.pack()

tk.Button(root, text="Get Weather", command=fetch\_and\_display\_weather).pack(pady=10)

output\_label \= tk.Label(root, text="", justify="left")  
output\_label.pack(pady=10)

root.mainloop()

---

#### **`weather.py`**

import requests

API\_KEY \= "YOUR\_API\_KEY"  \# Replace this with your OpenWeatherMap key  
BASE\_URL \= "https://api.openweathermap.org/data/2.5/weather"

def get\_current\_weather(city):  
    params \= {"q": city, "appid": API\_KEY, "units": "metric"}  
    response \= requests.get(BASE\_URL, params=params)  
      
    if response.status\_code \!= 200:  
        raise Exception("City not found or API error.")  
      
    return response.json()

---

#### **`storage.py`**

import json  
import os  
from datetime import datetime

DATA\_DIR \= "data"

def save\_weather\_data(city, data):  
    os.makedirs(DATA\_DIR, exist\_ok=True)  
    filename \= os.path.join(DATA\_DIR, f"{city.lower().replace(' ', '\_')}.json")  
    entry \= {  
        "timestamp": datetime.now().isoformat(),  
        "weather": data  
    }

    if os.path.exists(filename):  
        with open(filename, "r") as f:  
            history \= json.load(f)  
    else:  
        history \= \[\]

    history.append(entry)

    with open(filename, "w") as f:  
        json.dump(history, f, indent=4)

---

Let me know when you’ve:

* Picked a name

* Pasted in the files

* Installed a free API key (I can help you sign up if needed)

Then we’ll move on to polishing & refactoring ✨  
 After that… character generation magic begins.

