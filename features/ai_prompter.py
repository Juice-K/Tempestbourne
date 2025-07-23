# Ai Prompter
# features/ai_prompter.py

def generate_prompt(race, char_class, alignment, gender, weather_data):
    """
    Generate a vivid prompt string for a character image based on race, class, alignment, gender, and weather.
    This prompt is designed to work well with DALL·E or other AI image generators.
    """
    weather_desc = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    wind = weather_data['wind']['speed']

    temp_descriptor = (
        "icy" if temp < 5 else
        "misty" if temp < 15 else
        "breezy" if wind > 20 else
        "sun-drenched" if temp > 30 else
        "moody"
    )


    # Core prompt
    prompt = (
        f"A {alignment.lower()} {race} {char_class} standing in a {temp_descriptor} landscape, "
        f"with {weather_desc} swirling around them. This {gender_noun} is ready for battle — "
        f"cinematic style, fantasy lighting, detailed armor, epic atmosphere."
    )

    return prompt
