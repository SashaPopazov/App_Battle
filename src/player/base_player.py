from abc import ABC, abstractmethod


class BasePlayer(ABC):

    DEFAULT_HEALTH_FOR_PLAYER = 100
    DEFAULT_AND_HEALING_START_VALUE = 18
    DEFAULT_AND_HEALING_END_VALUE = 25
    LUCKY_START_VALUE = 10
    LUCKY_END_VALUE = 35

    @abstractmethod
    def default_damage(self, player):
        pass

    @abstractmethod
    def lucky_damage(self, player):
        pass

    @abstractmethod
    def healing(self, player):
        pass

    @property
    @abstractmethod
    def health(self):
        pass

    @health.setter
    @abstractmethod
    def health(self, value):
        pass

    @abstractmethod
    def get_random_action(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

