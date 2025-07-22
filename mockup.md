tempestbourne/
│
├── main.py                        # Launch GUI, handles user interaction
├── .env                           # Stores API keys (OpenWeatherMap, DALL·E, etc.)
├── requirements.txt               # All dependencies (tkinter, requests, pillow, etc.)
├── README.md
├── mockup.md                      # Visuals, sketches, or logic flow
│── starter_code.py                # Code for any additional features before implementation 

├── assets/                        # All visual/media assets
│   ├── gifs/                      # Race+Class-based animated GIFs
│   │   ├── elf_fighter.gif
│   │   ├── tiefling_bard.gif
│   │   └── ...
│   └── templates/                 # PDF/character sheet templates (if needed)
││   │   └── README.md

├── data/                          # Weather samples, saved characters, logs
│   ├── sample_weather.json
│   ├── generated_characters.json
│   └── log.txt
│
├── features/                      # App logic modules (core brains)
│   │   └── init
│   ├── character_generator.py     # Builds full character from weather + inputs
│   ├── weather_fetcher.py         # Pulls forecast data (city + random city)
│   ├── name_generator.py          # Race- and gender-based name logic
│   ├── bio_generator.py           # Creates 2-line backstory
│   ├── gif_selector.py            # Maps race/class to GIF asset
│   ├── ai_prompter.py             # Generates prompts for external AI tools
│   └── export_tools.py            # Saves to PDF or character sheets
│   ├── gif_generator.py           # Builds GIFs from code 
│
├── gui/                           # GUI elements (optional modular split)
│   │   └── init
│   ├── input_form.py              # Builds and validates user form
│   ├── character_gui.py           # gui for converting character into GIFs
│   ├── results_display.py         # Shows generated characters and GIFs
│   └── buttons.py                 # Export/save buttons
│   └── gif_preview_frame.py       # Gives logic for previewing GIFs

│
├── storage/                       # Local save/load (optional DB-style logic)
│   │   └── init
│   └── local_db.py                # Save/load character data
│
├── utils/                         # Constants, helpers, formatters
│   │   └── init
│   ├── constants.py               # Lists of races, classes, alignments, weather mappings
│   ├── formatters.py              # Helper functions for text, colors, etc.
│   └── validators.py              # Input validation, type checks, etc.
│
└── tests/                         # Future-proof: unit tests (if desired)
    └── test_character_gen.py


Ultimately, the GUI will allow players to:
  insert a City, Date, and Time, and Level and Gender of their choosing >
  the GUI will pull weather predictions for that time and for a random city (same Date and Time) >
  using the details of the predictions, the GUI will generate a character for the desired city and the random city (each character will be assigned 
    Race, 
    Class, 
    Alignment, 
    Hit Points, 
    Race-based Name, 
    Level-based Ability Scores, 
    Class-based skills, 
    Alignment-based Equipment, 
    2-line Bio or background text (using 5e gameplay as the standard)) >
  then the user can choose to save one or both of the outputs (PDF, Character Sheet, other...) 

At the end of this process, I'd think it'd be great if each character were represented by a Race+Class-based GIF so that the user can see an image. So, Gender will have to be another input. I'm nervous about this project because I'm definitely pushing my limits, but it may be a good opportunity to learn to use user inputs to generate prompts to AI tools. 