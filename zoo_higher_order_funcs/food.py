def make_get_animal_food(time_of_day="morning"):
    def _get_animal_food(animal):
        # time_of_day is morning or evening. Our animals like different things
        # for breakfast and dinner
        if animal in ["shark", "tuna", "dolphin"]:
            if time_of_day == "morning":
                return "sardines"
            else:
                return "herring"
        elif animal == "snake":
            if time_of_day == "morning":
                return "crickets"
            else:
                return "mice"
        elif animal == "tiger":
            if time_of_day == "morning":
                return "chicken"
            else:
                return "beef"
        elif animal == "gorilla":
            if time_of_day == "morning":
                return "bananas"
            else:
                return "grapes"

    return _get_animal_food
