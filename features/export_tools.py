# Export Tools
# features/export_tools.py

from reportlab.lib.pagesizes import letter   # pretty obvious - 8.5 inches x 11 inches or 612 points x 792 points
from reportlab.pdfgen import canvas   # for creating PDF files and treating them like a "canvas"
import os  # for file path operations 

def export_character_to_pdf(character_data: dict, filename: str = "tempestbourne_character.pdf"):
    """
    Generate a character sheet PDF from character data.
    """
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 50, "Tempestbourne Character Sheet")

    # Character Basics
    c.setFont("Helvetica", 12)
    y = height - 100
    spacing = 20

    c.drawString(50, y, f"Name: {character_data.get('name', 'N/A')}")
    y -= spacing
    c.drawString(50, y, f"Race: {character_data.get('race', 'N/A')}")
    y -= spacing
    c.drawString(50, y, f"Class: {character_data.get('char_class', 'N/A')}")
    y -= spacing
    c.drawString(50, y, f"Alignment: {character_data.get('alignment', 'N/A')}")
    y -= spacing
    c.drawString(50, y, f"HP: {character_data.get('hp', 'N/A')}")
    y -= spacing

    # Skills (optional: list-style)
    skills = character_data.get('skills', [])
    c.drawString(50, y, "Skills: " + ", ".join(skills))
    y -= spacing

    # Weather info
    c.drawString(50, y, f"Weather: {character_data.get('weather', 'Unknown')}")
    y -= spacing

    # Bio
    bio = character_data.get('bio', '')
    c.drawString(50, y, "Bio:")
    y -= spacing
    for line in bio.split('\n'):
        c.drawString(70, y, line)
        y -= spacing


    # Save PDF
    c.save()
    print(f"Character exported as: {filename}")


