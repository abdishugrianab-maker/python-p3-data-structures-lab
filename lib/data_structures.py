# Given data
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Returns a list of strings with the names of each spicy food."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns a list of dictionaries where heat_level is greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Outputs each spicy food in the format: Name (Cuisine) | Heat Level: 🌶..."""
    for food in spicy_foods:
        heat_emojis = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_emojis}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns a single dictionary for the spicy food whose cuisine matches."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no matching cuisine found

def print_spiciest_foods(spicy_foods):
    """Outputs ONLY the spicy foods with heat level > 5."""
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    """Returns an integer representing the average heat level."""
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_spicy_food):
    """Returns the original list with the new spicy_food added."""
    spicy_foods.append(new_spicy_food)
    return spicy_foods