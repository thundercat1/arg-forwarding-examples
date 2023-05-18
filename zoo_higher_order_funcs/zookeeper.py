def make_rounds(exhibits, get_animals, get_animal_food):
    for exhibit in exhibits:
        animals = get_animals(exhibit)
        for animal in animals:
            food = get_animal_food(animal)
            print(f"Feeding {animal} some {food}.")
