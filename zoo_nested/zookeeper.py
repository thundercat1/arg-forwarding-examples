from zoo_nested.exhibits import get_animals
from zoo_nested.food import get_animal_food


def make_rounds(exhibits, get_animals_kwargs, get_animal_food_kwargs):
    """

    Args:
        exhibits (List[str]): exhibits to visit. Make it jungle and aquarium or you'll be sorry.
        get_animals_kwargs (Dict[str, any]): The kwargs to forward to get_animals. See that function for details.
        get_animal_food_kwargs (Dict[str, any]): The kwargs to forward to get_animal_food. See that function for details.
    """
    for exhibit in exhibits:
        animals = get_animals(exhibit, **get_animals_kwargs)
        for animal in animals:
            food = get_animal_food(animal, **get_animal_food_kwargs)
            print(f"Feeding {animal} some {food}.")
