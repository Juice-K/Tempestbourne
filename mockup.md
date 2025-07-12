tempestbourne/
│
├── main.py                        # Launch GUI, handles user interaction
├── .env                           # Stores API keys (OpenWeatherMap, DALL·E, etc.)
├── requirements.txt               # All dependencies (tkinter, requests, pillow, etc.)
├── README.md
├── mockup.md                      # Visuals, sketches, or logic flow
│
├── assets/                        # All visual/media assets
│   ├── gifs/                      # Race+Class-based animated GIFs
│   │   ├── elf_fighter.gif
│   │   ├── tiefling_bard.gif
│   │   └── ...
│   └── templates/                 # PDF/character sheet templates (if needed)
│
├── data/                          # Weather samples, saved characters, logs
│   ├── sample_weather.json
│   ├── generated_characters.json
│   └── log.txt
│
├── features/                      # App logic modules (core brains)
│   ├── character_generator.py     # Builds full character from weather + inputs
│   ├── weather_fetcher.py         # Pulls forecast data (city + random city)
│   ├── name_generator.py          # Race- and gender-based name logic
│   ├── bio_generator.py           # Creates 2-line backstory
│   ├── gif_selector.py            # Maps race/class to GIF asset
│   ├── ai_prompter.py             # Generates prompts for external AI tools
│   └── export_tools.py            # Saves to PDF or character sheets
│
├── gui/                           # GUI elements (optional modular split)
│   ├── input_form.py              # Builds and validates user form
│   ├── results_display.py         # Shows generated characters and GIFs
│   └── buttons.py                 # Export/save buttons
│
├── storage/                       # Local save/load (optional DB-style logic)
│   └── local_db.py                # Save/load character data
│
├── utils/                         # Constants, helpers, formatters
│   ├── constants.py               # Lists of races, classes, alignments, weather mappings
│   ├── formatters.py              # Helper functions for text, colors, etc.
│   └── validators.py              # Input validation, type checks, etc.
│
└── tests/                         # Future-proof: unit tests (if desired)
    └── test_character_gen.py
