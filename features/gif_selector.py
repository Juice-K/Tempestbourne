# features/gif_selector.py

import os
import time
import requests
from io import BytesIO
from PIL import Image
import openai  # DALL·E 3 API
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import PLACEHOLDER_IMAGE_PATH, DEFAULT_IMAGE_SAVE_PATH, DEFAULT_GIF_OUTPUT_PATH

# === Config ===
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise EnvironmentError("Missing OpenAI API key in environment variables.")


# === Prompt Builders ===
def generate_gif_prompt(character: dict) -> str:
    """
    Creates a vivid prompt from character attributes to be used with an AI GIF generator.
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


# === Image Generation (OpenAI) ===
def generate_image(prompt: str, save_path: str = DEFAULT_IMAGE_SAVE_PATH) -> str:
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
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        img = Image.open(BytesIO(image_response.content))
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        img.save(save_path)

        return save_path
    except Exception as e:
        print("[Error] Image generation failed:", e)
        return None


# === GIF Generation (Selenium + Ezgif) ===
def upload_to_ezgif_and_animate(image_path: str, output_path: str = DEFAULT_GIF_OUTPUT_PATH) -> str:
    """
    Automates GIF animation via ezgif.com using Selenium.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://ezgif.com/effects")
        wait = WebDriverWait(driver, 10)

        file_input = wait.until(EC.presence_of_element_located((By.NAME, "new-image")))
        file_input.send_keys(os.path.abspath(image_path))
        driver.find_element(By.NAME, "upload").click()

        wait.until(EC.presence_of_element_located((By.ID, "tool-form")))
        driver.find_element(By.NAME, "effect[]").click()  # Default to "shake"
        driver.find_element(By.NAME, "apply").click()

        time.sleep(6)
        result_gif = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='output']//img"))
        )
        gif_url = result_gif.get_attribute("src")
        if gif_url.startswith("//"):
            gif_url = "https:" + gif_url

        response = requests.get(gif_url)
        response.raise_for_status()

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(response.content)

        return output_path
    except Exception as e:
        print("[Error] GIF generation failed:", e)
        return None
    finally:
        driver.quit()


# === Unified Generator ===
def create_animated_character_gif(character_data: dict) -> str:
    """
    Creates a GIF from character data via OpenAI + Ezgif automation.
    """
    prompt = generate_gif_prompt(character_data)
    image_path = generate_image(prompt)
    if not image_path:
        return None
    gif_path = upload_to_ezgif_and_animate(image_path)
    return gif_path


# === Mock/Placeholder Tools ===
def get_image_from_openai(prompt, save_path=DEFAULT_IMAGE_SAVE_PATH):
    """
    Mock version of image generation (for local testing without API calls).
    """
    print(f"[Mock] Generating image with prompt: {prompt}")
    if os.path.exists(PLACEHOLDER_IMAGE_PATH):
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(PLACEHOLDER_IMAGE_PATH, 'rb') as src, open(save_path, 'wb') as dst:
            dst.write(src.read())
    return save_path

def get_gif_placeholder(character_data):
    """
    Placeholder function for image + future gif.
    """
    prompt = generate_gif_prompt(character_data)
    image_path = get_image_from_openai(prompt)
    return {
        "prompt": prompt,
        "image_path": image_path,
        "status": "Image ready, GIF animation pending (ezgif.com)"
    }

def generate_gif_from_prompt(prompt: str) -> str:
    """
    Future integration stub with external video-to-GIF generator tools.
    """
    print("Sending prompt to GIF generator (stub):", prompt)
    return "data/gifs/placeholder.gif"
