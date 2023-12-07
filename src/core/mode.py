import json

from core.hero import Hero
from core.race import Race


class Mode:
    def __init__(self, name, config_path, tab_widget):
        self.name = name
        self.tab_widget = tab_widget
        self.heroes_dict = {}
        self.races = []
        self.load_data(config_path)

    def load_data(self, config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            for race in data["Races"]:
                race_obj = Race(race["Name"], race["Heroes"])
                self.races.append(race_obj)
                for hero in race_obj.heroes:
                    self.heroes_dict[hero.name] = hero

    def get_races(self):
        return [race.name for race in self.races]

    def get_heroes_by_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race.heroes
        return None

    def get_hero_by_name(self, hero_name):
        return self.heroes_dict.get(hero_name)

    def get_tab_widget(self):
        return self.tab_widget
