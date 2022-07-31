import random


class Game():
    colors = ["red", "yellow", "green", "blue"]
    current_card = None

    def center_card(self):
        self.current_card = {random.randint(0, 9): random.choice(self.colors)}

    def __init__(self):
        self.center_card()
