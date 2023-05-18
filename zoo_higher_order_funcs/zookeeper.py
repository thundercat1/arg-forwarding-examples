from zoo_higher_order_funcs.exhibits import make_get_animals
from zoo_higher_order_funcs.food import make_get_animal_food

# We don't have to do it this way, but optionally can re-export the functions from child modules
# so that users can just import everything they need from one place.
make_get_animals = make_get_animals
make_get_animal_food = make_get_animal_food


def make_rounds(exhibits, get_animals, get_animal_food):
    """...

    Args:
        exhibits (List[str]): exhibits to visit. Make it jungle and aquarium or you'll be sorry.
        get_animals (Callable): Function that takes an exhibit name and returns a list of animals.
            You probably want to use make_get_animals to construct it.
        get_animal_food (Callable): Function that takes an animal name and returns a food.
            You probably want to use make_get_animal_food to construct it.
    """
    for exhibit in exhibits:
        animals = get_animals(exhibit)
        for animal in animals:
            food = get_animal_food(animal)
            print(f"Feeding {animal} some {food}.")
