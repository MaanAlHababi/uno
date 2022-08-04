import random


class Game():
    colors = ["red", "yellow", "green", "blue"]
    colored_cards = ["+2", "skip", "reverse"]
    wild_cards = [{"wild": "+4"}, {"wild": "wild"}]

    pack = []

    current_card = None

    def center_card(self):
        card = random.choice(self.pack)
        self.current_card = card
        self.pack.remove(card)

    @staticmethod
    def prepare_pack():
        for color in Game.colors:
            for i in Game.colored_cards:
                Game.pack.append({i: color})

        for i in range(0, 4):
            for wild_card in Game.wild_cards:
                Game.pack.append(wild_card)

        Game.pack *= 2

    def __init__(self):
        for i in range(0, 10):
            Game.colored_cards.append((str(i)))
        self.prepare_pack()
        self.center_card()