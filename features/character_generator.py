# Character Generator
import random
from utils.constants import RACES, CLASSES, ALIGNMENTS, WEATHER_TO_TRAITS, WEATHER_MAIN_TO_CLASSES 
from utils.constants import WEATHER_CODE_TO_RACE


        # double check for correct imports / imports subject to change depending on randomized performance
class Character:
    def __init__(self, name, gender, race, char_class, alignment, hp, level, stats, skills, equipment, bio, gif_path):
        self.name = name
        self.gender = gender
        self.race = race
        self.char_class = char_class
        self.alignment = alignment
        self.hp = hp
        self.level = level
        self.stats = stats
        self.skills = skills
        self.equipment = equipment
        self.bio = bio
        self.gif_path = gif_path

    def to_dict(self):
        return vars(self)

def generate_character(weather_data, level, gender):
    """
    Generate a 5e character based on weather and user input.
    """
    description = weather_data['weather'][0]['description'].lower()
    temperature = weather_data['main']['temp']
    wind_speed = weather_data['wind']['speed']

    # --- Trait Decisions ---
    race = choose_race(weather_data)
    char_class = choose_class(weather_data) 
    alignment = choose_alignment(description)
    name = generate_name(race, gender)
    hp = calculate_hp(char_class, level)
    stats = generate_ability_scores(level)
    skills = choose_skills(char_class)
    equipment = choose_equipment(alignment)
    bio = generate_bio(race, char_class, alignment, weather_data)

    # --- Prompt & GIF Generation ---
    character_stub = Character(
        name=name, gender=gender, race=race, char_class=char_class, alignment=alignment,
        hp=hp, level=level, stats=stats, skills=skills, equipment=equipment, bio=bio,
        gif_path=None
    )

    prompt = generate_prompt_from_character(character_stub, weather_data)
    filename = f"{race}_{char_class}_{alignment}_{random.randint(1000,9999)}.gif".replace(" ", "_")
    save_path = os.path.join("assets/gifs", filename)

    try:
        generate_gif(prompt, save_path)
        gif_path = save_path
    except Exception as e:
        print(f"[GIF ERROR] Using fallback GIF instead — {e}")
        gif_path = get_gif_path(race, char_class)  # fallback

    return Character(
        name, gender, race, char_class, alignment, hp, level,
        stats, skills, equipment, bio, gif_path
    )

def choose_race(weather_data):
    code = weather_data["weather"][0]["id"]
    return WEATHER_CODE_TO_RACE.get(code, random.choice(RACES))


    # filler functions for trait decisions (see utils/constants.py)
    # subject to change depending on randomized performance

def choose_class(weather_data):
    main = weather_data["weather"][0]["main"]
    wind = weather_data.get("wind", {}).get("speed", 0)
    temp = weather_data.get("main", {}).get("temp", 20)

    # Pull themed options from main weather type
    candidates = WEATHER_MAIN_TO_CLASSES.get(main, CLASSES)

    # Optional: spice it up with temp/wind
    if wind > 15 and "Monk" in candidates:
        return "Monk"
    elif temp < 0 and "Cleric" in candidates:
        return "Cleric"
    elif temp > 30 and "Barbarian" in candidates:
        return "Barbarian"

    return random.choice(candidates)

def choose_alignment(description):
    for keyword in WEATHER_TO_TRAITS:
        if keyword in description:
            return WEATHER_TO_TRAITS[keyword]["alignment"]
    return random.choice(ALIGNMENTS)


def generate_name(race, gender):
    # Use name_generator.py soon!
    return f"{race}_{gender}_Name"

def calculate_hp(char_class, level):
    hit_die = {
        "Fighter": 10, "Wizard": 6, "Rogue": 8, "Cleric": 8, "Barbarian": 12
    }.get(char_class, 8)
    return hit_die + (hit_die // 2 * (level - 1))

def generate_ability_scores(level):
    base = [8, 10, 12, 13, 14, 15]
    random.shuffle(base)
    return dict(zip(["STR", "DEX", "CON", "INT", "WIS", "CHA"], base))

def choose_skills(char_class):
    return ["Perception", "Athletics"]  # Temporary filler

def choose_equipment(alignment):
    return ["Backpack", "Rope", "Torch"]  # Temporary filler

def generate_bio(race, char_class, alignment, weather_data):
    return f"A {alignment.lower()} {race.lower()} {char_class.lower()} shaped by {weather_data['weather'][0]['description']} skies."

def get_gif_path(race, char_class):
    return f"assets/gifs/{race.lower()}_{char_class.lower()}.gif"


