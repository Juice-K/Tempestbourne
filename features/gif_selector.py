# Gif Selector
# features/gif_selector.py

# features/gif_selector.py

import os
import openai  # openai library for DALL·E 3 API
from PIL import Image  # Pillow for image handling
from io import BytesIO  # from io module for handling byte streams 

# Set your API key (keep this secure!)
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_character_prompt(character_data):
    """
    Generate a cinematic prompt for DALL·E 3 based on character data.
    """
    weather = character_data.get("weather_desc", "mysterious weather")
    race = character_data.get("race", "fantasy figure")
    class_ = character_data.get("class", "adventurer")
    alignment = character_data.get("alignment", "neutral")
    weapon = character_data.get("weapon", "a signature weapon")
    mood = character_data.get("mood", "intense determination")

    return (
        f"A {alignment.lower()} {race.lower()} {class_.lower()} with {weather} around them. "
        f"They're wielding {weapon.lower()} and radiating {mood.lower()} energy. "
        "Fantasy art, detailed, cinematic lighting."
    )

def generate_image(prompt, save_path="temp_character_image.png"):
    """
    Send the prompt to DALL·E 3 and save the returned image to disk.
    """
    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url

        # Download image from URL
        image_response = openai._client.get(image_url)
        img = Image.open(BytesIO(image_response.content))
        img.save(save_path)

        return save_path
    except Exception as e:
        print("Error generating or saving image:", e)
        return None

def get_gif_placeholder(character_data):
    """
    Future: Animate the image or convert via ezgif automation.
    """
    prompt = create_character_prompt(character_data)
    image_path = generate_image(prompt)

    # Placeholder return
    return {
        "prompt": prompt,
        "image_path": image_path,
        "status": "Image ready, GIF animation pending (ezgif.com)"
    }


# placeholder for future integration with AI-powered GIF generation tools (from ChatGPT)
# subject to modification w/ future comments and changes)
"""
GIF Selector Module
-------------------
Generates descriptive prompts from character data for use with AI-powered GIF generation tools.
Includes placeholders for future integration with external video/GIF APIs (e.g., Pika Labs, RunwayML).
"""

def generate_gif_prompt(character: dict) -> str:
    """
    Creates a vivid prompt from character attributes to be used with an AI GIF generator.
    
    Parameters:
        character (dict): Dictionary containing character info such as race, class, alignment, traits, and equipment.
    
    Returns:
        str: A detailed textual prompt.
    """
    race = character.get("race", "Unknown race")
    char_class = character.get("class", "Adventurer")
    alignment = character.get("alignment", "Neutral")
    traits = character.get("traits", [])
    weapons = character.get("equipment", {}).get("weapons", [])
    level = character.get("level", 1)

    prompt = (
        f"A short animated GIF of a level {level} {alignment} {race} {char_class}. "
        f"The character is influenced by traits like {', '.join(traits)}. "
        f"They wield {' and '.join(weapons) if weapons else 'no visible weapons'}. "
        "Style: high fantasy, slightly stylized, loopable 2-second action pose. "
        "Ideal for use in a DnD character visual showcase."
    )
    return prompt


def generate_gif_from_prompt(prompt: str) -> str:
    """
    Placeholder for future integration with an AI video-to-GIF generator.
    
    Parameters:
        prompt (str): The descriptive prompt to send to an AI GIF tool.
    
    Returns:
        str: Path or URL to the generated GIF. Currently returns placeholder path.
    """
    # TODO: Integrate with external API or local video-to-GIF workflow.
    print("Sending prompt to GIF generator (stub):", prompt)

    # Example placeholder path for testing purposes
    fake_gif_path = "data/gifs/placeholder.gif"
    return fake_gif_path
