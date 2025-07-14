import random
from utils.constants import WEATHER_CODE_TO_RACE, RACES 


    # this was a ChatGPT suggestion in case anything goes wrong with the dictionary it made
def get_race_from_weather_code(code):
    return WEATHER_CODE_TO_RACE.get(code, random.choice(RACES))
