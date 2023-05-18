def make_get_animals(
    *, is_gorilla_at_doctor: bool = False, num_snake_eggs_hatched: int = 0
):
    def _get_animals(
        exhibit: str,
    ):
        if exhibit == "aquarium":
            return ["shark", "tuna", "dolphin"]
        elif exhibit == "jungle":
            animals = ["snake", "tiger"]
            if not is_gorilla_at_doctor:
                animals.append("gorilla")
            for _ in range(num_snake_eggs_hatched):
                animals.append("snake")

        return animals

    return _get_animals
