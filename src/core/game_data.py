import json

from core.race import Race


class GameData:
    def __init__(self, config_path):
        self.races = []
        self.heroes_dict = {}
        self.load_data(config_path)

    def load_data(self, config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            for race in data["Races"]:
                race_obj = Race(race["Name"], race["Heroes"])
                self.races.append(race_obj)
                for hero in race_obj.heroes:
                    self.heroes_dict[hero.name] = hero

    def get_heroes_by_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race.heroes
        return None

    def get_hero_by_name(self, hero_name):
        return self.heroes_dict.get(hero_name)
