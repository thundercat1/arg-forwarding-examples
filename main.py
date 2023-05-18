# Here, in order to know what to pass to make_rounds, you need to know the signatures
# of the functions that it calls. It's hard to know what defaults they have, and you
# don't get help from your editor constructing these dictionaries.

# If get_animals changes its signature and you don't update your call, you'll
# get a stacktrace pointing to an error in zookeeper.py, which counterintuitively
# is not the place that you'll need to change to fix the error.

import zoo_nested.zookeeper as nested_zookeeper

print("\nFeeding animals with nested functions. \n\n")
get_animals_kwargs = {"is_gorilla_at_doctor": True}
get_animal_food_kwargs = {"time_of_day": "evening"}
nested_zookeeper.make_rounds(
    ["aquarium", "jungle"], get_animals_kwargs, get_animal_food_kwargs
)

###############################################################################


# Here, you had to do some extra imports, but now you can set the get_animals and
# get_animal_food parameters directly, and you get help from your editor constructing
# the args

# If there's a problem with the arguments you're passing to get_animals, the stack
# trace will point here because you're calling it directly.

from zoo_higher_order_funcs.zookeeper import (
    make_rounds,
    make_get_animal_food,
    make_get_animals,
)

print("\nFeeding animals with higher order functions. \n\n")
animal_getter = make_get_animals(is_gorilla_at_doctor=True, num_snake_eggs_hatched=13)
food_getter = make_get_animal_food(time_of_day="evening")
make_rounds(["aquarium", "jungle"], animal_getter, food_getter)

###############################################################################

# Here, again, extra imports, but the animal and food configuration pararmeters are
# set directly instead of being forwarded through the zookeeper function.

from zoo_objects.zookeeper import make_rounds, AnimalGetter, FoodGetter

print("\nFeeding animals with objects. \n\n")
animal_getter = AnimalGetter(is_gorilla_at_doctor=True, num_snake_eggs_hatched=2)
food_getter = FoodGetter(time_of_day="evening")
make_rounds(["aquarium", "jungle"], animal_getter, food_getter)
