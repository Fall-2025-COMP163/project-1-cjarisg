"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Clayan Ariaga
Date: 11/13/2025

AI Usage: ChatGPT assisted with debugging file read/write formatting and project structure.
"""

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class == "Warrior":
        strength = 10 + (level * 5)
        magic = 2 + (level * 1)
        health = 100 + (level * 10)
    elif character_class == "Mage":
        strength = 3 + (level * 2)
        magic = 12 + (level * 5)
        health = 80 + (level * 6)
    elif character_class == "Rogue":
        strength = 7 + (level * 3)
        magic = 6 + (level * 2)
        health = 70 + (level * 5)
    elif character_class == "Cleric":
        strength = 6 + (level * 3)
        magic = 10 + (level * 4)
        health = 95 + (level * 8)
    else:
        strength, magic, health = 5, 5, 50
    return strength, magic, health


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        print("Error: Invalid class name.")
        return None

    level = 1
    gold = 100
    strength, magic, health = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character


def save_character(character, filename):
    """
    Saves character to text file in specific format
    """
    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()


def load_character(filename):
    """
    Loads character from text file and returns as dictionary
    """
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    data = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            data[key.strip()] = value.strip()

    # Convert back into dictionary form
    character = {
        "name": data["Character Name"],
        "class": data["Class"],
        "level": int(data["Level"]),
        "strength": int(data["Strength"]),
        "magic": int(data["Magic"]),
        "health": int(data["Health"]),
        "gold": int(data["Gold"])
    }
    return character


def display_character(character):
    """
    Prints formatted character sheet
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================")


def level_up(character):
    """
    Increases character level and recalculates stats
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 50
    return character


# Optional demo block for local testing
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")
    if hero:
        save_character(hero, "aria.txt")
        new_hero = load_character("aria.txt")
        level_up(new_hero)
        display_character(new_hero)
