# Press the green button in the gutter to run the script.
from src.battle.battlefield import Battlefield
from src.player.player import Player

if __name__ == '__main__':
    player = Player('You', 150)
    computer = Player('Computer', 150)

    battlefield = Battlefield([player, computer])
    winner = battlefield.start_game()
