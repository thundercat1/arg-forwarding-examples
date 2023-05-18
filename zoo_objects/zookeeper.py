def make_rounds(exhibits, animal_getter, food_getter):
    for exhibit in exhibits:
        animals = animal_getter.get_animals(exhibit)
        for animal in animals:
            food = food_getter.get_food(animal)
            print(f"Feeding {animal} some {food}.")
