"""
COMP 163 - Project 1: Character Creator & Chronicles
Author: Clayan Ariaga
AI assistance: ChatGPT assisted with structuring file I/O, stat formulas,
and debugging compatibility with COMP163 autograder.
"""

# ==============================
#  CHARACTER CREATION FUNCTIONS
# ==============================

def calculate_stats(character_class, level):
    """Calculate strength, magic, and health based on class and level."""
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
    """Create a new character dictionary with calculated stats."""
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        print("Error: Invalid class name.")
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold,
    }


def save_character(character, filename):
    """Save a character to a text file in the official COMP 163 format."""
    try:
        with open(filename, "w") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
        return True
    except Exception as e:
        print("Error saving character:", e)
        return False


def load_character(filename):
    """Load character data from file and return a standardized dictionary."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return None

    data = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            data[key.strip()] = value.strip()

    try:
        return {
            "name": data.get("Character Name", ""),
            "class": data.get("Class", ""),
            "level": int(data.get("Level", 1)),
            "strength": int(data.get("Strength", 0)),
            "magic": int(data.get("Magic", 0)),
            "health": int(data.get("Health", 0)),
            "gold": int(data.get("Gold", 0)),
        }
    except Exception as e:
        print("Error loading character:", e)
        return None


def level_up(character):
    """Increase the character's level and recalculate stats."""
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 50
    return character


def display_character(character):
    """Print character info neatly."""
    print(f"Character Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


# ==============================
#  DEMO EXECUTION (optional)
# ==============================
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")
    if hero:
        display_character(hero)
        save_character(hero, "aria.txt")
        loaded = load_character("aria.txt")
        if loaded:
            print("\nLoaded character:")
            display_character(loaded)
        print("\nLeveling up character...")
        leveled = level_up(hero)
        display_character(leveled)
