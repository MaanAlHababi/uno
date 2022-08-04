import random


class Game():
    colors = ["red", "yellow", "green", "blue"]
    colored_cards = ["+2", "skip", "reverse"]

    pack = []

    current_card = None

    def center_card(self):
        card = random.choice(self.pack)
        self.current_card = card
        self.pack.remove(card)

    def prepare_pack(self):
        for i in range(0, 10):
            self.colored_cards.append((str(i)))

        for color in self.colors:
            for i in self.colored_cards:
                self.pack.append({i: color})

        self.pack *= 2

        for i in range(0, 4):
            self.pack.append({"+4"})
            self.pack.append({"wild"})

    def __init__(self):
        self.prepare_pack()
        self.center_card()