from game import Game
from cards import *

import random


class Player():
    deck = None

    def generate_deck(self):
        self.deck = []
        for i in range(7):
            card = random.choice(Game.pack)
            self.deck.append(Cards(card))
            Game.pack.remove(card)

        return self.deck

    def __init__(self):
        self.generate_deck()


class BotPlayer(Player):
    def __init__(self):
        super().__init__()

    def play_turn(self):
        return random.randint(0, len(self.deck)-1)