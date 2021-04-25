from src.player.base_player import BasePlayer
import random
from random import randint
import copy


class Player(BasePlayer):

    def __init__(self, name, health=None):
        if health is None:
            self.health = self.DEFAULT_HEALTH_FOR_PLAYER
        else:
            self.health = health
        self.actions = [Player.default_damage, Player.lucky_damage, Player.healing]
        self.name = name
        self.start_health = self.health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Deal default damage to an enemy in the range of 18-25
    def default_damage(self, player):
        print("\nCall default hit")
        default_result = random.randint(self.DEFAULT_AND_HEALING_START_VALUE, self.DEFAULT_AND_HEALING_END_VALUE)
        player.health -= default_result
        if player.health < 0:
            player.health = 0

    # Deal lucky damage to an enemy in the range of 10-35
    def lucky_damage(self, player):
        print("\nCall lucky hit")
        lucky_result = random.randint(self.LUCKY_START_VALUE, self.LUCKY_END_VALUE)
        player.health -= lucky_result
        if player.health < 0:
            player.health = 0

    # Heal in the range of 18-25
    def healing(self, player):
        print("\nCall healing")
        healing_result = random.randint(self.DEFAULT_AND_HEALING_START_VALUE, self.DEFAULT_AND_HEALING_END_VALUE)
        self.health += healing_result
        if self.health > self.start_health:
            self.health = self.start_health

    # Random choice of player action
    def get_random_action(self):
        """When the health of the Computer reaches 35%, its chance of healing increases."""
        if (self.health * 100) / self.start_health <= 35 and self.name == 'Computer':
            new_actions = copy.copy(self.actions)
            new_actions.extend([Player.healing, Player.healing, Player.healing])
            return new_actions[randint(0, len(new_actions)-1)]
        """The chance remains the same"""
        return self.actions[randint(0, len(self.actions)-1)]





