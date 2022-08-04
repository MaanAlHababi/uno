import random

from game import Game


class Cards:
    def __init__(self, value_as_dict):
        self.value_as_dict = value_as_dict

    @staticmethod
    def draw(lst):
        card = random.choice(Game.pack)
        lst.append(Cards(card))
        Game.pack.remove(card)
        return lst

    @staticmethod
    def check_wild_card(c):
        # print(list(c.keys())[0]) # Amazing for debugging
        if list(c.keys())[0] == "wild":
            return True

        return False

    def check_same_number(self, g, card):
        if list(self.value_as_dict.keys())[0] == list(g.current_card.keys())[0]:
            return card

        else:
            # print("Wrong number")
            return False

    def check_color(self, g, card, lst):
        # print(card, g.current_card)
        if not Cards.check_wild_card(g.current_card):
            if not Cards.check_wild_card(card.value_as_dict):
                if list(card.value_as_dict.values())[0] == list(g.current_card.values())[0]:
                    return card

                else:
                    # print("Wrong color")
                    if self.check_same_number(g, card):
                        return self.check_same_number(g, card)

            else:
                return True

        else:
            return True

        return False

class Colored_Cards(Cards):
    cards = [random.randint(0, 9), "+2", "skip", "reverse"]

class ActionCards(Cards):
    cards = ["+4", "wild"]