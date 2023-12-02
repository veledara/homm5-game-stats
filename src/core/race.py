from core.hero import Hero


class Race:
    def __init__(self, name, heroes):
        self.name = name
        self.heroes = [Hero(hero["Name"], hero["ImagePath"]) for hero in heroes]
