# features/gif_generator.py

import os
import time
import openai
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set your OpenAI API key
OPENAI_API_KEY = os.getenv("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")  
def generate_image(prompt, output_path="generated_image.png"):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    image_data = requests.get(image_url).content
    with open(output_path, 'wb') as f:
        f.write(image_data)
    return output_path

def animate_image_with_ezgif(image_path, effect="shake"):
    # Setup headless browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        # Upload to ezgif
        driver.get("https://ezgif.com/" + effect)
        upload_input = driver.find_element(By.NAME, "new-image")
        upload_input.send_keys(os.path.abspath(image_path))
        driver.find_element(By.ID, "upload-form").submit()

        # Wait for processing and click 'Submit'
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "file")))
        driver.find_element(By.XPATH, "//form//input[@type='submit']").click()

        # Wait for result and get the result URL
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "video")))
        gif_element = driver.find_element(By.CLASS_NAME, "video")
        gif_url = gif_element.find_element(By.TAG_NAME, "img").get_attribute("src")

        # Download GIF
        gif_data = requests.get(gif_url).content
        gif_path = "animated_character.gif"
        with open(gif_path, 'wb') as f:
            f.write(gif_data)

        return gif_path

    finally:
        driver.quit()

