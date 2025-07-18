# Name Generator
import random

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


# Testing the ChatGPT name-bank-style logic of grouping names by race and gender 

import random

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



# Scaffolded NAME_BANKS covering all WEATHER_CODE_TO_RACE entries
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

def generate_name(race: str, gender: str) -> str:
    try:
        bank = NAME_BANKS.get(race, {})
        names = bank.get(gender, [])
        return random.choice(names) if names else "Nameless One"
    except Exception as e:
        print(f"[NameGen Error] {e}")
        return "Unknown"

if __name__ == "__main__":
    # Quick smoke-test
    print(generate_name("Elf", "Female"))


