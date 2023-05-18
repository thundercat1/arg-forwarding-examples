from dataclasses import dataclass


@dataclass
class AnimalGetter:
    is_gorilla_at_doctor: bool = False
    num_snake_eggs_hatched: int = 0

    def get_animals(
        self,
        exhibit: str,
    ):
        if exhibit == "aquarium":
            return ["shark", "tuna", "dolphin"]
        elif exhibit == "jungle":
            animals = ["snake", "tiger"]
            if not self.is_gorilla_at_doctor:
                animals.append("gorilla")
            for _ in range(self.num_snake_eggs_hatched):
                animals.append("snake")

        return animals
