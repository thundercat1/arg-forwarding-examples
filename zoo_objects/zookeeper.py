from zoo_objects.food import FoodGetter
from zoo_objects.exhibits import AnimalGetter

# We don't have to do it this way, but optionally can re-export the classes from child modules
# so that users can just import everything they need from one place.
FoodGetter = FoodGetter
AnimalGetter = AnimalGetter


def make_rounds(exhibits, animal_getter, food_getter):
    for exhibit in exhibits:
        animals = animal_getter.get_animals(exhibit)
        for animal in animals:
            food = food_getter.get_food(animal)
            print(f"Feeding {animal} some {food}.")
