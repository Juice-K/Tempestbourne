# Character Generator
import random
from utils.constants import RACES, CLASSES, ALIGNMENTS, WEATHER_TO_TRAITS

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
    race = choose_race(description, temperature)
    char_class = choose_class(description, wind_speed)
    alignment = choose_alignment(description)
    name = generate_name(race, gender)
    hp = calculate_hp(char_class, level)
    stats = generate_ability_scores(level)
    skills = choose_skills(char_class)
    equipment = choose_equipment(alignment)
    bio = generate_bio(race, char_class, alignment, weather_data)
    gif_path = get_gif_path(race, char_class)

    return Character(
        name, gender, race, char_class, alignment, hp, level,
        stats, skills, equipment, bio, gif_path
    )

    # filler functions for trait decisions (see utils/constants.py)
    # subject to change depending on randomized performance
def choose_race(description, temperature):
    # Example stub: if it's cold, lean toward Dwarves or Goliaths
    return random.choice(RACES)

def choose_class(description, wind_speed):
    return random.choice(CLASSES)

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


