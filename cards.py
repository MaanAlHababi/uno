import random

from game import Game


class Cards:
    def __init__(self, value_as_dict):
        self.value_as_dict = value_as_dict

    def draw(self, lst):
        card = random.choice(Game.pack)
        lst.append(Cards(card))
        Game.pack.remove(card)
        return lst

    def check_same_number(self, lst, g, card):
        if list(self.value_as_dict.keys())[0] == list(g.current_card.keys())[0]:
            return card

        else:
            # print("Wrong number")
            self.draw(lst)

    def check_color(self, lst, g, card):
        # print(card, g.current_card)
        if list(self.value_as_dict.values())[0] == list(g.current_card.values())[0]:
            return card

        else:
            # print("Wrong color")
            if self.check_same_number(lst, g, card):
                return self.check_same_number(lst, g, card)


class Colored_Cards(Cards):
    cards = [random.randint(0, 9), "+2", "skip", "reverse"]

class ActionCards(Cards):
    cards = ["+4", "wild"]