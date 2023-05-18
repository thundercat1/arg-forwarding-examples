from dataclasses import dataclass


@dataclass
class FoodGetter:
    time_of_day: str = "morning"

    def get_food(self, animal):
        # time_of_day is morning or evening. Our animals like different things
        # for breakfast and dinner
        if animal in ["shark", "tuna", "dolphin"]:
            if self.time_of_day == "morning":
                return "sardines"
            else:
                return "herring"
        elif animal == "snake":
            if self.time_of_day == "morning":
                return "crickets"
            else:
                return "mice"
        elif animal == "tiger":
            if self.time_of_day == "morning":
                return "chicken"
            else:
                return "beef"
        elif animal == "gorilla":
            if self.time_of_day == "morning":
                return "bananas"
            else:
                return "grapes"
