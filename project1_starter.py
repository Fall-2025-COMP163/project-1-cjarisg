# COMP 163 - Project 1: Character Creator & Chronicles
# Author: Clayan Ariaga
# AI assistance used for code explanation and debugging.
# This file implements all required functions for the text-based RPG project.

# -------------------------------------------------------
# FUNCTION: calculate_stats
# -------------------------------------------------------

def calculate_stats(character_class, level):
    """Calculate strength, magic, and health based on class and level."""
    cls = character_class.lower()

    if cls == "warrior":
        strength = 10 + 2 * level
        magic = 3 + level
        health = 20 + 3 * level

    elif cls == "mage":
        strength = 4 + level
        magic = 12 + 3 * level
        health = 15 + level

    elif cls == "rogue":
        strength = 7 + 2 * level
        magic = 7 + 2 * level
        health = 12 + level

    elif cls == "cleric":
        strength = 6 + level
        magic = 10 + 2 * level
        health = 18 + 2 * level

    else:
        raise ValueError("Invalid character class.")

    return strength, magic, health


# -------------------------------------------------------
# FUNCTION: create_character
# -------------------------------------------------------

def create_character(name, character_class):
    """Create & return a character dictionary."""

    valid_classes = ["warrior", "mage", "rogue", "cleric"]
    cls = character_class.lower()

    if cls not in valid_classes:
        print(f"Error: '{character_class}' is not a valid class.")
        return None

    level = 1
    gold = 0

    strength, magic, health = calculate_stats(cls, level)

    character = {
        "name": name,
        "class": cls,       # store lowercase for consistency
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character


# -------------------------------------------------------
# FUNCTION: save_character
# -------------------------------------------------------

def save_character(character, filename):
    """Save character information to a text file."""
    with open(filename, "w") as f:
        f.write(f"Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")


# -------------------------------------------------------
# FUNCTION: load_character
# -------------------------------------------------------

def load_character(filename):
    """Load character data from a save file."""
    data = {}

    with open(filename, "r") as f:
        for line in f:
            if ": " in line:
                key, value = line.strip().split(": ", 1)

                key = key.lower()  # convert "Name" → "name"

                if key in ["level", "strength", "magic", "health", "gold"]:
                    value = int(value)

                data[key] = value

    # Return dictionary in exact expected format
    return {
        "name": data.get("name"),
        "class": data.get("class"),
        "level": data.get("level"),
        "strength": data.get("strength"),
        "magic": data.get("magic"),
        "health": data.get("health"),
        "gold": data.get("gold"),
    }


# -------------------------------------------------------
# FUNCTION: display_character
# -------------------------------------------------------

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


# -------------------------------------------------------
# FUNCTION: level_up
# -------------------------------------------------------

def level_up(character):
    """Increase level and recalc stats."""
    character["level"] += 1

    strength, magic, health = calculate_stats(character["class"], character["level"])

    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    print(f"{character['name']} leveled up to Level {character['level']}!")
    return character


# -------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------

if __name__ == "__main__":
    print("Welcome to Character Creator & Chronicles!")
    name = input("Enter your character's name: ").strip()

    print("Choose your class: Warrior, Mage, Rogue, Cleric")
    cls = input("Class: ").strip().lower()

    hero = create_character(name, cls)

    if hero:
        display_character(hero)
        save_file = f"{name.lower()}_save.txt"
        save_character(hero, save_file)
        print(f"Character saved to {save_file}.")
