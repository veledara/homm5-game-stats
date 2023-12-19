class Game:
    def __init__(
        self,
        mode,
        player_hero,
        enemy_hero,
        win_state,
        date,
        player_name,
        enemy_name,
        notes,
    ):
        self.mode = mode
        self.player_hero = player_hero
        self.enemy_hero = enemy_hero
        self.win_state = win_state
        self.date = date
        self.player_name = player_name
        self.enemy_name = enemy_name
        self.notes = notes
