from game import Game
import random


class Player():
    deck = None

    def generate_deck(self):
        self.deck = []
        for i in range(7):
            self.deck.append({random.randint(0, 9): random.choice(Game.colors)})

        return self.deck

    def __init__(self):
        self.generate_deck()
