from random import randint
from src.player.base_player import BasePlayer
from typing import List, Optional


class Battlefield:

    def __init__(self, players: List[BasePlayer]):
        self.players = players
        self.battle_area: List[BasePlayer] = []

    def start_game(self):
        print("Game is starting...\n")
        """The game will not start until there are at least 2 players in the battlefield"""
        if len(self.players) < 2:
            raise Exception('Player length must be greater then 1!')

        while len(self.players) != 1:
            self.push_random_player_to_battle_area()
            self.push_random_player_to_battle_area()
            self.start_battle()
            self.rollback()
        return self.players[0]

    # Adding a random player from those already created to the battlefield
    def push_random_player_to_battle_area(self):
        random_player = self.players[randint(0, len(self.players)-1)]
        self.battle_area.append(random_player)

        self._exclude(random_player)

    # Exclusion from the list of possible participants in the battle of that player
    # from the already created ones who has already been added to the battlefield
    def _exclude(self, player_to_exclude: BasePlayer):
        for idx, player in enumerate(self.players):
            if player.name == player_to_exclude.name:
                self.players.pop(idx)

    def start_battle(self):
        if len(self.battle_area) == 2:

            """Random selection of the first participant"""
            active_player = self.battle_area[randint(0, len(self.battle_area) - 1)]
            passive_player: Optional[BasePlayer] = None

            """Adding the remaining participant"""
            for idx, player in enumerate(self.battle_area):
                if player.name != active_player.name:
                    passive_player = player
            if passive_player is None:
                raise Exception("Target player not found!")

            """Random choice of the player's move"""
            action = active_player.get_random_action()
            action(active_player, passive_player)
            print(f'Attacking_player_{active_player.name} - {active_player.health}')
            print(f'Dormant_player_{passive_player.name} - {passive_player.health}')

    def rollback(self):
        for idx, player in enumerate(self.battle_area):
            if player.health <= 0:
                self.battle_area.pop(idx)
                print("\nGame ended!")

        self.players = self.players + self.battle_area
        self.battle_area = []

