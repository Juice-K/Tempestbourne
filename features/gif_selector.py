# Gif Selector
# features/gif_selector.py

# features/gif_selector.py

import os
import openai  # openai library for DALL·E 3 API
from PIL import Image  # Pillow for image handling
from io import BytesIO  # from io module for handling byte streams 
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# features/gif_selector.py
def get_character_gif(character):
    # Placeholder: Eventually will call DALL·E + ezgif automation
    return "assets/gifs/goliath_barbarian.gif"


def generate_gif_prompt(character_data):
    return (
        f"A {character_data['alignment']} {character_data['race']} {character_data['class']} "
        f"with weather matching {character_data['weather_description']}. "
        f"Wielding {character_data['weapon']} and radiating {character_data['vibe']} energy."
    )

def get_image_from_openai(prompt, save_path="temp_image.png"):
    # Placeholder for OpenAI DALL·E API integration
    # This should generate and save an image locally
    print(f"[Mock] Generating image with prompt: {prompt}")
    # Example: just copy a local placeholder image for now
    placeholder_path = "assets/placeholder_image.png"
    if os.path.exists(placeholder_path):
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(placeholder_path, 'rb') as src, open(save_path, 'wb') as dst:
            dst.write(src.read())
    return save_path

def upload_to_ezgif_and_animate(image_path, output_path="generated/animated_character.gif"):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://ezgif.com/effects")
        wait = WebDriverWait(driver, 10)

        # Upload the image
        file_input = wait.until(EC.presence_of_element_located((By.NAME, "new-image")))
        file_input.send_keys(os.path.abspath(image_path))
        driver.find_element(By.NAME, "upload").click()

        # Wait for next page
        wait.until(EC.presence_of_element_located((By.ID, "tool-form")))

        # Apply simple effect
        driver.find_element(By.NAME, "effect[]").click()  # Default to "shake"
        driver.find_element(By.NAME, "apply").click()

        # Wait for GIF to render
        time.sleep(6)
        result_gif = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='output']//img"))
        )
        gif_url = result_gif.get_attribute("src")

        # Download the GIF
        if gif_url.startswith("//"):
            gif_url = "https:" + gif_url
        response = requests.get(gif_url)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path

    except Exception as e:
        print(f"[Error] GIF generation failed: {e}")
        return None

    finally:
        driver.quit()

def create_animated_character_gif(character_data):
    prompt = generate_gif_prompt(character_data)
    image_path = get_image_from_openai(prompt)
    gif_path = upload_to_ezgif_and_animate(image_path)
    return gif_path


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
