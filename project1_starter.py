"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Clayan Ariaga
Date: 11/13/2025

AI Usage: ChatGPT assisted with debugging and formatting to match COMP 163 project specifications.
"""

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)

    Design:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
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
    return (strength, magic, health)


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold

    Example:
    char = create_character("Aria", "Mage")
    """
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        print("Error: Invalid class name.")
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100

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

    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    f = open(filename, "w")
    f.write(f"Character Name: {character['name']}\n")
    f.write(f"Class: {character['class']}\n")
    f.write(f"Level: {character['level']}\n")
    f.write(f"Strength: {character['strength']}\n")
    f.write(f"Magic: {character['magic']}\n")
    f.write(f"Health: {character['health']}\n")
    f.write(f"Gold: {character['gold']}\n")
    f.close()


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    data = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            data[key.strip()] = value.strip()

    character = {
        "name": data.get("Character Name", ""),
        "class": data.get("Class", ""),
        "level": int(data.get("Level", 1)),
        "strength": int(data.get("Strength", 0)),
        "magic": int(data.get("Magic", 0)),
        "health": int(data.get("Health", 0)),
        "gold": int(data.get("Gold", 0))
    }

    return character


def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
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
    Modifies the character dictionary directly
    Returns: updated character
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 50
    return character


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    hero = create_character("Aria", "Mage")
    if hero:
        display_character(hero)
        save_character(hero, "aria.txt")
        print("\nCharacter saved successfully!")
        loaded = load_character("aria.txt")
        print("\nLoaded character:")
        display_character(loaded)
        print("\nAfter leveling up:")
        level_up(hero)
        display_character(hero)
