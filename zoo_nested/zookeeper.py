from zoo_nested.exhibits import get_animals
from zoo_nested.food import get_animal_food


def make_rounds(exhibits, get_animals_kwargs, get_animal_food_kwargs):
    for exhibit in exhibits:
        animals = get_animals(exhibit, **get_animals_kwargs)
        for animal in animals:
            food = get_animal_food(animal, **get_animal_food_kwargs)
            print(f"Feeding {animal} some {food}.")
