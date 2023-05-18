from zoo_higher_order_funcs.exhibits import make_get_animals
from zoo_higher_order_funcs.food import make_get_animal_food

# We don't have to do it this way, but optionally can re-export the functions from child modules
# so that users can just import everything they need from one place.
make_get_animals = make_get_animals
make_get_animal_food = make_get_animal_food


def make_rounds(exhibits, get_animals, get_animal_food):
    for exhibit in exhibits:
        animals = get_animals(exhibit)
        for animal in animals:
            food = get_animal_food(animal)
            print(f"Feeding {animal} some {food}.")
