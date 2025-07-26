tempestbourne/
│
├── main.py                        # Launch GUI, handles user interaction
├── .env                           # Stores API keys (OpenWeatherMap, DALL·E, etc.)
├── .gitignore
├── requirements.txt               # All dependencies (tkinter, requests, pillow, etc.)
├── README.md
├── mockup.md                      # Visuals, sketches, or logic flow
│── starter_code.py                # Code for any additional features before implementation 

├── assets/                        # All visual/media assets
│   ├── fonts/                     # Fonts
│   ├── images/                    # Race+Class-based animated GIFs
│   │   ├── .keep
│   │   ├── placeholder.gif
│   └── templates/                 # PDF/character sheet templates (if needed)
│   │   └── README.md

├── data/                          # Weather samples, saved characters, logs
│   ├── sample_weather.json
│   ├── generated_characters.json
│   └── log.txt
│
├── features/                      # App logic modules (core brains)
│   │   └── __init__.py
│   ├── character_generator.py     # Builds full character from weather + inputs
│   ├── weather_fetcher.py         # Pulls forecast data (city + random city)
│   ├── name_generator.py          # Race- and gender-based name logic
│   ├── bio_generator.py           # Creates 2-line backstory
│   └── export_tools.py            # Saves to PDF or character sheets
│
├── gui/                           # GUI elements (optional modular split)
│   │   └── __init__.py
│   ├── input_form.py              # Builds and validates user form
│   ├── character_gui.py           # gui for converting character into GIFs
│   ├── results_display.py         # Shows generated characters and GIFs
│   └── gif_preview_frame.py       # Gives logic for previewing GIFs

│
├── storage/                       # Local save/load (optional DB-style logic)
│   │   └── __init__.py
│   ├── local_db.py                # Save/load character data
│   └── gifs                       # GIFs folder
│   └── pdfs                       # PDFs folder

│
├── utils/                         # Constants, helpers, formatters
│   │   └── __init__.py
│   ├── constants.py               # Lists of races, classes, alignments, weather mappings
│   ├── helper.py                  # Helper functions for text, colors, etc.
│   └── validators.py              # Input validation, type checks, etc.
│
└── tests/                         # Future-proof: unit tests (if desired)
    └── test_character_gen.py
    └── tests_print_statements.py  # List of print statements for testing (accidentally wiped, needs updating)



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