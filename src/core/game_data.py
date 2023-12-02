import json

from core.race import Race


class GameData:
    def __init__(self, config_path):
        self.races = []
        self.load_data(config_path)

    def load_data(self, config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.races = [Race(race["Name"], race["Heroes"]) for race in data["Races"]]

    def get_heroes_by_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race.heroes
        return None
