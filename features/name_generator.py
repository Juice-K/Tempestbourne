# Name Generator
# this feature not currently in use
import random

# from name_generator import generate_name
# from name_generator import get_random_name


# Testing the ChatGPT name-bank-style logic of grouping names by race and gender 
# Sample name banks — expand these over time
# NAME_BANKS = {
#     "Elf": {
#         "Male": ["Aelar", "Faelar", "Theren", "Varis"],
#         "Female": ["Adrie", "Shanairra", "Thia", "Keyleth"],
#         "Nonbinary": ["Laeroth", "Syllin", "Naeris", "Myriil"]
#     },
#     "Tiefling": {
#         "Male": ["Zherxik", "Kael", "Akmenos", "Lucian"],
#         "Female": ["Lyxiss", "Irae", "Nemeia", "Vex"],
#         "Nonbinary": ["Rhogur", "Xarrah", "Saelihn", "Drakos"]
#     },
#     "Human": {
#         "Male": ["Jareth", "Tomas", "Cedric", "Rowan"],
#         "Female": ["Elira", "Mira", "Kara", "Seraphine"],
#         "Nonbinary": ["Lior", "Nyx", "Arden", "Quinlan"]
#     },
#     # Add more races as needed
# }

# def generate_name(race: str, gender: str) -> str:
#     try:
#         names = NAME_BANKS.get(race, {}).get(gender, [])
#         if not names:
#             return "Nameless One"
#         return random.choice(names)
#     except Exception as e:
#         print(f"Name generation error: {e}")
#         return "Unknown"

# # Example for testing
# if __name__ == "__main__":
#     print(generate_name("Elf", "Nonbinary"))



import random

# Scaffolded NAME_BANKS covering all WEATHER_CODE_TO_RACE entries
# name banks expanded to cover more options
# left this function out of capstone version, but left in place for future use
NAME_BANKS = {
    "Half-Orc":       {"Male": [], "Female": [], "Nonbinary": []},
    "Kenku":          {"Male": [], "Female": [], "Nonbinary": []},
    "Gnome":          {"Male": [], "Female": [], "Nonbinary": []},
    "Locathah":       {"Male": [], "Female": [], "Nonbinary": []},
    "Shadar-kai":     {"Male": [], "Female": [], "Nonbinary": []},
    "Autognome":      {"Male": [], "Female": [], "Nonbinary": []},
    "Triton":         {"Male": [], "Female": [], "Nonbinary": []},
    "Warforged":      {"Male": [], "Female": [], "Nonbinary": []},
    "Owlin":          {"Male": [], "Female": [], "Nonbinary": []},
    "Half-Elf":       {"Male": [], "Female": [], "Nonbinary": []},
    "Kobold":         {"Male": [], "Female": [], "Nonbinary": []},
    "Dwarf":          {"Male": [], "Female": [], "Nonbinary": []},
    "Hadozee":        {"Male": [], "Female": [], "Nonbinary": []},
    "Loxodon":        {"Male": [], "Female": [], "Nonbinary": []},
    "Tortle":         {"Male": [], "Female": [], "Nonbinary": []},
    "Harengon":       {"Male": [], "Female": [], "Nonbinary": []},
    "Verdan":         {"Male": [], "Female": [], "Nonbinary": []},
    "Hexblood":       {"Male": [], "Female": [], "Nonbinary": []},
    "Tiefling":       {"Male": [], "Female": [], "Nonbinary": []},
    "Grung":          {"Male": [], "Female": [], "Nonbinary": []},
    "Dhampir":        {"Male": [], "Female": [], "Nonbinary": []},
    "Githzerai":      {"Male": [], "Female": [], "Nonbinary": []},
    "Changeling":     {"Male": [], "Female": [], "Nonbinary": []},
    "Yuan-Ti Pureblood":{"Male": [], "Female": [], "Nonbinary": []},
    "Halfling":       {"Male": [], "Female": [], "Nonbinary": []},
    "Leonin":         {"Male": [], "Female": [], "Nonbinary": []},
    "Aarakocra":      {"Male": [], "Female": [], "Nonbinary": []},
    "Thri-kreen":     {"Male": [], "Female": [], "Nonbinary": []},
    "Satyr":          {"Male": [], "Female": [], "Nonbinary": []},
    "Goblin":         {"Male": [], "Female": [], "Nonbinary": []},
    "Hobgoblin":      {"Male": [], "Female": [], "Nonbinary": []},
    "Kalashtar":      {"Male": [], "Female": [], "Nonbinary": []},
    "Eladrin":        {"Male": [], "Female": [], "Nonbinary": []},
    "Dragonborn":     {"Male": [], "Female": [], "Nonbinary": []},
    "Shifter":        {"Male": [], "Female": [], "Nonbinary": []},
    "Sea Elf":        {"Male": [], "Female": [], "Nonbinary": []},
    "Elf":            {"Male": [], "Female": [], "Nonbinary": []},
    "Vedalken":       {"Male": [], "Female": [], "Nonbinary": []},
    "Genasi":         {"Male": [], "Female": [], "Nonbinary": []},
    "Orc":            {"Male": [], "Female": [], "Nonbinary": []},
    "Bugbear":        {"Male": [], "Female": [], "Nonbinary": []},
    "Fairy":          {"Male": [], "Female": [], "Nonbinary": []},
    "Plasmoid":       {"Male": [], "Female": [], "Nonbinary": []},
    "Reborn":         {"Male": [], "Female": [], "Nonbinary": []},
    "Firbolg":        {"Male": [], "Female": [], "Nonbinary": []},
    "Lizardfolk":     {"Male": [], "Female": [], "Nonbinary": []},
    "Astral Elf":     {"Male": [], "Female": [], "Nonbinary": []},
    "Tabaxi":         {"Male": [], "Female": [], "Nonbinary": []},
    "Centaur":        {"Male": [], "Female": [], "Nonbinary": []},
    "Githyanki":      {"Male": [], "Female": [], "Nonbinary": []},
    "Goliath":        {"Male": [], "Female": [], "Nonbinary": []},
    "Minotaur":       {"Male": [], "Female": [], "Nonbinary": []},
    "Simic Hybrid":   {"Male": [], "Female": [], "Nonbinary": []},
    "Human":          {"Male": [], "Female": [], "Nonbinary": []},
    "Aasimar":        {"Male": [], "Female": [], "Nonbinary": []},
}

# version for pulling random names from specific libraries (will require variable modification) 
NAME_BANKS["Dragonborn"] = {
    "Male": [
        "Arjhan", "Balasar", "Donaar", "Ghesh", "Heskan",
        "Kriv", "Medrash", "Mehen", "Nadarr", "Pandjed",
        "Patrin", "Rhogar", "Shamash", "Tarhun", "Torinn"
    ],
    "Female": [
        "Akra", "Biri", "Daar", "Farideh", "Harann",
        "Flavilar", "Jheri", "Kava", "Korinn", "Mishann",
        "Nala", "Perra", "Raiann", "Sora", "Thava"
    ],
    "Nonbinary": [
        "Zorinn", "Therax", "Kavash", "Araska", "Vireth",
        "Darven", "Laskhar", "Nymosh", "Rhaz", "Tarnok"
    ]
}

NAME_BANKS["Dwarf"] = {
    "Male": [
        "Adrik", "Baern", "Barendd", "Brottor", "Dain",
        "Darrak", "Delg", "Eberk", "Einkil", "Fargrim",
        "Flint", "Gardain", "Harbek", "Kildrak", "Orsik"
    ],
    "Female": [
        "Amber", "Artin", "Audhild", "Bardryn", "Dagnal",
        "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda",
        "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd"
    ],
    "Nonbinary": [
        "Thorbryn", "Marnor", "Vragga", "Lodran", "Durra",
        "Khorla", "Bergrin", "Skalda", "Durnik", "Yorla"
    ]
}

NAME_BANKS["Halfling"] = {
    "Male": [
        "Alton", "Ander", "Cade", "Corrin", "Eldon",
        "Errich", "Finnan", "Garret", "Lyle", "Milo",
        "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"
    ],
    "Female": [
        "Andry", "Bree", "Callie", "Cora", "Euphemia",
        "Jillian", "Kithri", "Lavinia", "Lidda", "Merla",
        "Nedda", "Paela", "Portia", "Seraphina", "Trym"
    ],
    "Nonbinary": [
        "Fenni", "Rindle", "Tavi", "Marny", "Hollow",
        "Quinnic", "Belba", "Nibs", "Elbi", "Siv"
    ]
}

NAME_BANKS["Elf"] = {
    "Male": [
        "Adran", "Aelar", "Aramil", "Arannis", "Aust",
        "Berrian", "Carric", "Erevan", "Galinndan", "Hadarai",
        "Immeral", "Ivellios", "Laucian", "Mindartis", "Thamior"
    ],
    "Female": [
        "Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua",
        "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna",
        "Felosial", "Ielenia", "Keyleth", "Lia", "Shanairra"
    ],
    "Nonbinary": [
        "Sylvaris", "Lethril", "Nymerel", "Thirion", "Vaelis",
        "Orlith", "Saryndel", "Zelphar", "Ilanys", "Elaran"
    ]
}

NAME_BANKS["Human"] = {
    "Male": [
        "Alric", "Bastian", "Cedric", "Dorian", "Edric",
        "Falk", "Garrick", "Hadrian", "Jareth", "Kaelen",
        "Lucan", "Merric", "Rowan", "Tomas", "Wesric"
    ],
    "Female": [
        "Aveline", "Briala", "Celeste", "Delara", "Elira",
        "Fiona", "Gwenna", "Isolde", "Kara", "Liora",
        "Mira", "Nerida", "Selene", "Talia", "Ysolde"
    ],
    "Nonbinary": [
        "Arden", "Cyran", "Ellis", "Kaelin", "Lior",
        "Nyx", "Quinlan", "Soren", "Talen", "Virel"
    ]
}

NAME_BANKS["Tiefling"] = {
    "Male": [
        "Akmenos", "Barakas", "Damakos", "Ekemon", "Iados",
        "Kairon", "Mordai", "Reth", "Skamos", "Zepar",
        "Xarzith", "Vassago", "Thamuz", "Lorcan", "Zherxik"
    ],
    "Female": [
        "Akta", "Anakis", "Bryseis", "Criella", "Damaia",
        "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia",
        "Orianna", "Phelaia", "Rieta", "Syra", "Vex"
    ],
    "Nonbinary": [
        "Rhogur", "Xarrah", "Saelihn", "Vyre", "Eilaz",
        "Thazar", "Nyrris", "Savael", "Drakos", "Tessith"
    ]
}

NAME_BANKS.update({
    "Orc": {
        "Male": [
            "Gorg", "Hruk", "Karg", "Thok", "Zug",
            "Drok", "Grish", "Rok", "Snag", "Brug"
        ],
        "Female": [
            "Urgra", "Shara", "Grishna", "Mogha", "Thura",
            "Zagra", "Brakka", "Draka", "Skara", "Ghra"
        ],
        "Nonbinary": [
            "Grek", "Zhak", "Snur", "Thrak", "Druk"
        ]
    },
    "Half-Orc": {
        "Male": [
            "Karn", "Rogar", "Thal", "Durn", "Mog",
            "Brak", "Gorun", "Harg", "Zul", "Krag"
        ],
        "Female": [
            "Shaara", "Vara", "Kara", "Mara", "Dasha",
            "Lura", "Thara", "Zara", "Brina", "Gara"
        ],
        "Nonbinary": [
            "Vrek", "Tharn", "Zaruk", "Mogran", "Gral"
        ]
    },
    "Goblin": {
        "Male": [
            "Snix", "Grik", "Zik", "Krik", "Bruk",
            "Drak", "Snik", "Trak", "Gluk", "Zrok"
        ],
        "Female": [
            "Snika", "Grika", "Zika", "Krika", "Bruka",
            "Draka", "Snika", "Trika", "Gluka", "Zroka"
        ],
        "Nonbinary": [
            "Snik", "Zuk", "Grix", "Triz", "Kruz"
        ]
    },
    "Hobgoblin": {
        "Male": [
            "Vark", "Hurk", "Grak", "Darg", "Thrak",
            "Zarn", "Krug", "Drak", "Farn", "Ghar"
        ],
        "Female": [
            "Vara", "Hura", "Grara", "Dara", "Thara",
            "Zara", "Kara", "Dina", "Fara", "Gara"
        ],
        "Nonbinary": [
            "Vrak", "Hrak", "Ghar", "Drak", "Thar"
        ]
    },
    "Bugbear": {
        "Male": [
            "Brug", "Gronk", "Thruk", "Drak", "Grak",
            "Snar", "Zrog", "Krog", "Mog", "Hruk"
        ],
        "Female": [
            "Bruga", "Grona", "Thruka", "Draka", "Graka",
            "Snara", "Zroga", "Kroga", "Moga", "Hruka"
        ],
        "Nonbinary": [
            "Gruk", "Thrak", "Zruk", "Druk", "Snark"
        ]
    },
    "Goliath": {
        "Male": [
            "Karn", "Thar", "Brak", "Durn", "Grun",
            "Hark", "Zorn", "Marn", "Grok", "Varn"
        ],
        "Female": [
            "Kara", "Thara", "Braka", "Durna", "Gruna",
            "Harka", "Zorna", "Marna", "Groka", "Varna"
        ],
        "Nonbinary": [
            "Vrek", "Tharn", "Grak", "Zarn", "Drak"
        ]
    },
    "Lizardfolk": {
        "Male": [
            "Sszark", "Thiss", "Zil", "Krith", "Ssik",
            "Griss", "Drak", "Viss", "Kriss", "Ssik"
        ],
        "Female": [
            "Sszira", "Thissa", "Zila", "Kritha", "Ssika",
            "Grissa", "Draka", "Vissa", "Krissa", "Ssika"
        ],
        "Nonbinary": [
            "Ssik", "Zik", "Drik", "Krik", "Vrik"
        ]
    }
})

NAME_BANKS.update({
    "Fairy": {
        "Male": [
            "Aeluin", "Branor", "Caelen", "Darian", "Elric",
            "Faelar", "Galan", "Irin", "Lorien", "Sylas"
        ],
        "Female": [
            "Aeris", "Briala", "Caelia", "Elyndra", "Faelina",
            "Lunara", "Melora", "Nyssa", "Sylva", "Thalia"
        ],
        "Nonbinary": [
            "Alaric", "Faren", "Lioren", "Sylas", "Tarian"
        ]
    },
    "Harengon": {
        "Male": [
            "Bran", "Crispin", "Dovak", "Finch", "Hopper",
            "Jasper", "Lazlo", "Marin", "Rinn", "Tobin"
        ],
        "Female": [
            "Belladonna", "Clover", "Daphne", "Felicity", "Juniper",
            "Lily", "Maribel", "Nissa", "Rosie", "Tansy"
        ],
        "Nonbinary": [
            "Bram", "Dale", "Jory", "Keir", "Taran"
        ]
    },
    "Eladrin": {
        "Male": [
            "Aerendyl", "Caelthas", "Eryndor", "Faelar", "Laucian",
            "Melwas", "Mythran", "Rolen", "Theren", "Vaelis"
        ],
        "Female": [
            "Ariya", "Caelynn", "Elanil", "Faelynn", "Lathlaeril",
            "Melwen", "Nymeria", "Serenya", "Thalia", "Vaela"
        ],
        "Nonbinary": [
            "Alariel", "Faelivrin", "Lethril", "Sylph", "Zyrel"
        ]
    },
    "Sea Elf": {
        "Male": [
            "Aeron", "Cyrion", "Davorin", "Lirien", "Nerath",
            "Orion", "Ralen", "Sylorin", "Thalor", "Varin"
        ],
        "Female": [
            "Alira", "Calithil", "Elysia", "Lirael", "Merina",
            "Neritha", "Sylra", "Talira", "Vereen", "Zylla"
        ],
        "Nonbinary": [
            "Aeris", "Darian", "Lioren", "Sylas", "Tarin"
        ]
    },
    "Shadar-kai": {
        "Male": [
            "Drevan", "Kalen", "Malrik", "Ravik", "Thalen",
            "Vaeril", "Xandar", "Zalric", "Zerik", "Zyran"
        ],
        "Female": [
            "Althaea", "Driana", "Kalis", "Lyris", "Malira",
            "Nyssara", "Selara", "Velyra", "Zalira", "Zyra"
        ],
        "Nonbinary": [
            "Aeris", "Kaelen", "Lorien", "Sylas", "Zyrel"
        ]
    },
    "Firbolg": {
        "Male": [
            "Brennar", "Calden", "Durnan", "Eldrin", "Faldor",
            "Garrik", "Haldor", "Keldon", "Merrin", "Thaden"
        ],
        "Female": [
            "Branna", "Calira", "Drena", "Eldira", "Faldira",
            "Garra", "Halira", "Kelira", "Merra", "Thalia"
        ],
        "Nonbinary": [
            "Bren", "Cal", "Dren", "Eld", "Fal"
        ]
    },
    "Centaur": {
        "Male": [
            "Arion", "Belen", "Calder", "Darius", "Faelan",
            "Galen", "Kaelen", "Loran", "Theron", "Veren"
        ],
        "Female": [
            "Alara", "Briella", "Calina", "Daria", "Faela",
            "Galia", "Kaela", "Lora", "Thera", "Vera"
        ],
        "Nonbinary": [
            "Ael", "Bryn", "Cal", "Dra", "Fael"
        ]
    }
})

NAME_BANKS.update({
    "Aasimar": {
        "Male": ["Caelion", "Zoriel", "Theron", "Elydran", "Malchior"],
        "Female": ["Seraphine", "Thalindra", "Auriel", "Nyxara", "Velistra"],
        "Nonbinary": ["Solien", "Arzire", "Virel", "Eiren", "Nozari"]
    },
    "Genasi": {
        "Male": ["Kael", "Zarith", "Vonn", "Raelak", "Tharion"],
        "Female": ["Saphra", "Aeris", "Ignaya", "Caldra", "Nymira"],
        "Nonbinary": ["Zuren", "Tyrix", "Velka", "Orin", "Lazir"]
    },
    "Gith": {
        "Male": ["Vrak", "Zorrek", "Kuthar", "Nithrak", "Tharn"],
        "Female": ["Zelith", "Karrax", "Lurza", "Drineth", "Mizhara"],
        "Nonbinary": ["Tzarn", "Vritha", "Xelruk", "Jarneth", "Qel"]
    },
    "Gnome": {
        "Male": ["Fizzik", "Boddynock", "Nimble", "Tinker", "Zibber"],
        "Female": ["Wizzle", "Pippa", "Nyxie", "Tinka", "Franny"],
        "Nonbinary": ["Glim", "Zip", "Marnie", "Tib", "Rollo"]
    },
    "Warforged": {
        "Male": ["Ironclad", "Bolt", "Thorn", "Vector", "Anvil"],
        "Female": ["Circuit", "Glint", "Echo", "Nova", "Shielda"],
        "Nonbinary": ["Cipher", "Core", "Phase", "Unit-9", "Mesh"]
    },
    "Changeling": {
        "Male": ["Jyn", "Thade", "Evan", "Sil", "Rilen"],
        "Female": ["Vira", "Shai", "Tressa", "Mira", "Ylith"],
        "Nonbinary": ["Whisp", "Nyme", "Ash", "Quinn", "Loen"]
    },
    "Kalashtar": {
        "Male": ["Ruhan", "Veseth", "Kiran", "Thovan", "Melek"],
        "Female": ["Shaana", "Thavira", "Isen", "Nali", "Yezra"],
        "Nonbinary": ["Vael", "Dureth", "Lior", "Riveth", "Sona"]
    },
})

NAME_BANKS.update({
    "Tabaxi": {
        "Male": ["Claw-of-Dusk", "Howl-in-Reeds", "Swift-Talon", "Echo-in-Snow", "Jumps-the-Gap"],
        "Female": ["Whispers-at-Dawn", "Pounce-of-Moonlight", "Huntress-Beneath-Stars", "Flicker-of-Tail", "Sings-to-Wind"],
        "Nonbinary": ["Walks-in-Shadow", "Still-Water", "Chase-the-Light", "Eyes-of-Ember", "Sleeps-in-Trees"]
    },
    "Triton": {
        "Male": ["Korrash", "Varnan", "Pelion", "Thurok", "Maros"],
        "Female": ["Zalara", "Nymene", "Calithra", "Orisha", "Virella"],
        "Nonbinary": ["Auron", "Zariel", "Nethys", "Kelmar", "Syrren"]
    },
    "Minotaur": {
        "Male": ["Brak", "Toruk", "Draz", "Vornak", "Gorim"],
        "Female": ["Ravka", "Thura", "Brelka", "Zarn", "Molgra"],
        "Nonbinary": ["Korr", "Vakra", "Jurn", "Tharn", "Grek"]
    },
    "Kenku": {
        "Male": ["Click", "Rattle", "Echo", "Scratch", "Hush"],
        "Female": ["Whistle", "Croak", "Trill", "Chirp", "Screech"],
        "Nonbinary": ["Caw", "Rustle", "Clack", "Shush", "Flick"]
    },
    "Kobold": {
        "Male": ["Skit", "Drik", "Bazzik", "Kriv", "Snark"],
        "Female": ["Ziri", "Vexi", "Triss", "Nixi", "Brelka"],
        "Nonbinary": ["Klik", "Razz", "Zan", "Mik", "Yit"]
    },
    "Yuan-Ti": {
        "Male": ["Sszar", "Vethis", "Nashir", "Zekhul", "Thaz"],
        "Female": ["Zashara", "Sylsith", "Veysha", "Nithari", "Ossira"],
        "Nonbinary": ["Isskar", "Sethys", "Nyza", "Tharnis", "Khaeth"]
    },
    "Tortle": {
        "Male": ["Shello", "Granok", "Tork", "Molto", "Brunto"],
        "Female": ["Shellyra", "Tamiya", "Groka", "Bila", "Nokta"],
        "Nonbinary": ["Rokko", "Yurra", "Moko", "Tarn", "Zibba"]
    },
})

NAME_BANKS.update({
    "Fairy": {
        "Male": ["Thistlewhim", "Brambleshade", "Zephyrdew", "Flickerflint", "Wanderleaf"],
        "Female": ["Glimmerpetal", "Dewdrop", "Lunaria", "Faegrace", "Mosswhirl"],
        "Nonbinary": ["Twilightgleam", "Whimsyroot", "Mistwink", "Starglen", "Silversap"]
    },
    "Eladrin": {
        "Male": ["Thalion", "Aerendyl", "Velion", "Caerthas", "Saryndor"],
        "Female": ["Yllawen", "Faelara", "Irielle", "Nuala", "Thessara"],
        "Nonbinary": ["Eluneth", "Mythil", "Sylrin", "Orithil", "Vaeris"]
    },
    "Aasimar": {
        "Male": ["Cassiel", "Thamior", "Lucen", "Seraphan", "Aurex"],
        "Female": ["Solene", "Virelai", "Aracel", "Mireth", "Noema"],
        "Nonbinary": ["Zariel", "Ruvael", "Elyndor", "Caelis", "Halos"],
    },
    "Tiefling": {
        "Male": ["Azazel", "Malrik", "Zareth", "Kaelzor", "Dravik"],
        "Female": ["Lilix", "Nyxara", "Velmora", "Zeraphine", "Drazira"],
        "Nonbinary": ["Skirn", "Izzeth", "Vashar", "Kyrith", "Xarnis"]
    },
    "Changeling": {
        "Male": ["Shade", "Cymric", "Pell", "Thorne", "Neris"],
        "Female": ["Whispa", "Syla", "Eira", "Mirin", "Thalia"],
        "Nonbinary": ["Reven", "Ashen", "Vex", "Solin", "Dreem"]
    },
    "Dhampir": {
        "Male": ["Corvan", "Vladin", "Mirek", "Thorne", "Lucan"],
        "Female": ["Selene", "Virel", "Morga", "Tressa", "Nyss"],
        "Nonbinary": ["Ascar", "Ruvan", "Noct", "Velka", "Zheren"]
    },
    "Hexblood": {
        "Male": ["Thistal", "Groven", "Brelthorn", "Hexar", "Varn"],
        "Female": ["Ythra", "Velda", "Nimira", "Zessia", "Grenda"],
        "Nonbinary": ["Myxa", "Tharnis", "Zavik", "Wyrmra", "Ossith"]
    },
})

NAME_BANKS.update({
    "Air Genasi": {
        "Male": ["Zephiros", "Aeris", "Whispar", "Galeon", "Thyros"],
        "Female": ["Sylpha", "Vayra", "Breezea", "Mistralyn", "Elarra"],
        "Nonbinary": ["Skylen", "Vexair", "Namiir", "Orryn", "Whirl"]
    },
    "Earth Genasi": {
        "Male": ["Granith", "Torak", "Boulderfist", "Durog", "Sten"],
        "Female": ["Terrara", "Garnessa", "Brilla", "Moltra", "Kavra"],
        "Nonbinary": ["Rokk", "Onyx", "Velgrun", "Tharn", "Gravax"]
    },
    "Fire Genasi": {
        "Male": ["Ignan", "Vuldar", "Pyrrhus", "Ashkar", "Caelon"],
        "Female": ["Embera", "Kavira", "Solixa", "Fyrra", "Lazra"],
        "Nonbinary": ["Cindyr", "Flarex", "Volc", "Searin", "Pyraxis"]
    },
    "Water Genasi": {
        "Male": ["Neroth", "Cascade", "Marryn", "Drenik", "Coralor"],
        "Female": ["Tahlassa", "Miryss", "Oceana", "Serina", "Llyndra"],
        "Nonbinary": ["Aqen", "Drift", "Rivun", "Sevril", "Tide"],
    },
    "Githyanki": {
        "Male": ["Vazk", "Zarrin", "Kralk", "Yzran", "Thok"],
        "Female": ["Zithra", "Krasha", "Velza", "Ryyka", "Drenza"],
        "Nonbinary": ["Qorr", "Thaz", "Kren", "Xol", "Varn"],
    },
    "Githzerai": {
        "Male": ["Tarn", "Zeran", "Omrik", "Balir", "Saeth"],
        "Female": ["Lirra", "Menya", "Zeyna", "Ruhla", "Eshya"],
        "Nonbinary": ["Saev", "Qetha", "Zyn", "Arkan", "Thaal"]
    },
    "Shardmind": {
        "Male": ["Crystar", "Oblix", "Tharnix", "Glasser", "Karnite"],
        "Female": ["Shardra", "Velquinn", "Glissara", "Quenra", "Myxina"],
        "Nonbinary": ["Prism", "Klynthe", "Zerix", "Refract", "Silix"]
    }
})

NAME_BANKS.update({
    "Aasimar": {
        "Male": ["Caelum", "Lucian", "Thalor", "Orius", "Zephan"],
        "Female": ["Seraphine", "Amariel", "Caelira", "Lumina", "Elariel"],
        "Nonbinary": ["Solyn", "Virel", "Zhara", "Aural", "Radiant"]
    },
    "Eladrin": {
        "Male": ["Theren", "Calen", "Faelor", "Sylthas", "Auren"],
        "Female": ["Nyari", "Vaelora", "Syllune", "Elarra", "Illyra"],
        "Nonbinary": ["Mythir", "Qirael", "Lunor", "Vaelis", "Trineth"]
    },
    "Deep Gnome": {
        "Male": ["Nibbin", "Grivver", "Zundel", "Thim", "Klob"],
        "Female": ["Trilla", "Wizzle", "Norna", "Sibbi", "Darra"],
        "Nonbinary": ["Zib", "Crint", "Jivvi", "Plooz", "Snarn"]
    },
    "Kalashtar": {
        "Male": ["Velu", "Doshin", "Kiran", "Tashan", "Qorim"],
        "Female": ["Sahari", "Vireya", "Luma", "Nishka", "Tevani"],
        "Nonbinary": ["Qira", "Leshan", "Tyne", "Oriva", "Zelith"]
    },
    "Thri-Kreen": {
        "Male": ["Chikt", "Krrash", "T’rrn", "Zekkt", "Clikk"],
        "Female": ["S’krii", "Trik’cha", "K’til", "Zarraq", "Kr’neen"],
        "Nonbinary": ["Tikra", "Zirr", "Ch’cha", "Rik’tik", "N’kra"]
    },
    "Astral Elf": {
        "Male": ["Myrren", "Talyon", "Velor", "Xarion", "Elyth"],
        "Female": ["Saela", "Ylyra", "Alurea", "Thyssia", "Vaeni"],
        "Nonbinary": ["Quaris", "Zirael", "Ilun", "Elyra", "Starin"]
    },
    "Verdan": {
        "Male": ["Gribb", "Durnik", "Thizz", "Borkle", "Snazz"],
        "Female": ["Mippa", "Krivna", "Zuli", "Glooma", "Snigga"],
        "Nonbinary": ["Fizzik", "Gronka", "Snorp", "Tribby", "Jox"]
    }
})



def generate_name(race: str, gender: str) -> str:
    try:
        bank = NAME_BANKS.get(race, {})
        names = bank.get(gender, [])
        return random.choice(names) if names else "Nameless One"
    except Exception as e:
        print(f"[NameGen Error] {e}")
        return "Unknown"
    
def get_random_name(race, gender):
    # Placeholder logic
    return f"{race}_{gender}_Name"

# from name_generator import generate_name
# from name_generator import get_random_name



if __name__ == "__main__":
    # Quick smoke-test
    print(generate_name("Elf", "Female"))


