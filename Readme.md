# 🌩️ Tempestbourne

**Part weather science, part tabletop RPG, part creative storytelling tool.**

Tempestbourne is a Tkinter-based fantasy character generator that fuses **real-world weather forecasting** with **Dungeons & Dragons 5E mechanics**.  
Players input a city, date, time, level, and gender, and the app generates **two unique characters**—one from the chosen city, one from a random comparison city—both shaped by actual forecast data.

---

## ✨ Features

- **Weather-Driven Character Creation**  
  Uses live forecast data to influence race, class, alignment, skills, and gear.

- **Dual City Comparison**  
  See weather for both your chosen location and a random city at the same date/time.

- **Dynamic Visualizations**  
  - Ridgeline plot comparing both cities’ weather patterns (Matplotlib + Seaborn).  
  - Radial bar chart highlighting forecast stats.

- **Rich Character Sheets**  
  Each character includes:
  - Race & Class
  - Alignment
  - Level-based stats
  - Skills & background
  - Weather-influenced gear
  - Themed animated GIF
  - 2-line bio

- **Export Options**  
  Save characters as PDF or send them to [D&D Beyond](https://www.dndbeyond.com).

---

## 🖥️ How It Works

1. **Input Your Adventure Settings**  
   Enter:
   - City
   - Date & time
   - Character gender
   - Desired level

2. **Weather Fetch**  
   The app pulls forecast data for your city and a random comparison city.

3. **Character Generation**  
   The weather conditions influence race, class, skills, and more.

4. **Choose Your Champion**  
   Compare two characters side-by-side, including stats and weather visuals.

5. **Export & Play**  
   Save your favorite as a PDF or import to D&D Beyond.

---

## 📸 Screenshots

*(Coming Soon)*

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Tkinter** – GUI framework
- **Matplotlib & Seaborn** – Weather visualizations
- **Requests** – API calls
- **OpenWeather API** – Forecast data
- **Pandas** – Data handling
- **ReportLab** – PDF export

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tempestbourne.git
   cd tempestbourne
