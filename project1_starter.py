# COMP 163 - Project 1: Character Creator & Chronicles
# Author: Clayan Ariaga
# AI assistance used for code explanation and debugging.
# This file implements all required functions for the text-based RPG project.

# FUNCTION: calculate_stats
def calculate_stats(character_class, level):
    """Calculate strength, magic, and health based on class and level."""
    if character_class.lower() == "warrior":
        strength = 10 + 2 * level
        magic = 3 + level
        health = 20 + 3 * level
    elif character_class.lower() == "mage":
        strength = 4 + level
        magic = 12 + 3 * level
        health = 15 + level
    elif character_class.lower() == "rogue":
        strength = 7 + 2 * level
        magic = 7 + 2 * level
        health = 12 + level
    elif character_class.lower() == "cleric":
        strength = 6 + level
        magic = 10 + 2 * level
        health = 18 + 2 * level
    else:
        raise ValueError("Invalid character class.")
    return strength, magic, health


# FUNCTION: create_character
def create_character(name, character_class):
    """Create a character dictionary with initial stats."""
    level = 1
    gold = 0
    valid_classes = ["warrior", "mage", "rogue", "cleric"]

    if character_class.lower() not in valid_classes:
        print(f"Error: '{character_class}' is not a valid class.")
        return None

    strength, magic, health = calculate_stats(character_class, level)

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold,
    }


# FUNCTION: save_character
def save_character(character, filename):
    """Save character information to a text file in consistent format."""
    with open(filename, "w") as f:
        f.write(f"Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")


# FUNCTION: load_character
def load_character(filename):
    """Load character data from a text file and return as dictionary."""
    character = {}
    mapping = {
        "name": "name",
        "class": "class",
        "level": "level",
        "strength": "strength",
        "magic": "magic",
        "health": "health",
        "gold": "gold",
        "character name": "name"  # safety in case of old save style
    }

    with open(filename, "r") as f:
        for line in f:
            if ": " not in line:
                continue
            key, value = line.strip().split(": ", 1)
            key = key.strip().lower()
            if key in mapping:
                key = mapping[key]
            if key in ["level", "strength", "magic", "health", "gold"]:
                try:
                    value = int(value)
                except ValueError:
                    pass
            character[key] = value

    # ensure all keys exist
    for k in ["name", "class", "level", "strength", "magic", "health", "gold"]:
        character.setdefault(k, 0 if k != "name" and k != "class" else "")

    return character


# FUNCTION: display_character
def display_character(character):
    """Print character info neatly."""
    print("\n===== CHARACTER INFO =====")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("==========================\n")


# FUNCTION: level_up
def level_up(character):
    """Increase the character's level and recalculate stats."""
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print(f"{character['name']} leveled up to Level {character['level']}!")
    return character


# MAIN PROGRAM
if __name__ == "__main__":
    print("Welcome to Character Creator & Chronicles!")
    name = input("Enter your character's name: ").strip()
    print("Choose your class: Warrior, Mage, Rogue, or Cleric")
    char_class = input("Class: ").strip().capitalize()

    hero = create_character(name, char_class)
    if hero:
        display_character(hero)
        save_file = f"{name.lower()}_save.txt"
        save_character(hero, save_file)
        print(f"Character saved to {save_file}.")
