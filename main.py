import random
import time

from game import Game
from player import Player


# Set conditions
# Condition 1: Same color
# Condition 2: Same number

def draw(lst):
    colors = ["red", "yellow", "blue", "green"]
    card = {random.randint(0, 9): random.choice(colors)}
    lst.append(card)
    return lst

def check_same_number(lst, g, card):
    if list(card.keys())[0] == list(g.current_card.keys())[0]:
        return card

    else:
        print("Wrong number")
        draw(lst)

def check_color(lst, g, card):
    # print(card, g.current_card)
    if list(card.values())[0] == list(g.current_card.values())[0]:
        return card

    else:
        print("Wrong color")
        if check_same_number(lst, g, card):
            return check_same_number(lst, g, card)

def main(p_no):
    winner = False
    # Generate decks for each player
    players = []
    for i in range(p_no):
        players.append(Player())

    # Generate a game (center card)
    g = Game()

    # Play
    turns = len(players)
    turn = 0
    while not winner:
        print(g.current_card)
        time.sleep(1)  # pause
        print(f"Player {turn+1}\'s turn.")
        print(players[turn].deck)
        time.sleep(1)  # pause
        play = int(input(f"Enter a number from 0-{len(players[turn].deck)-1} \n"))
        time.sleep(1)  # pause
        if not check_color(players[turn].deck, g, players[turn].deck[play]):
            turn += 1
            if turn >= turns:
                turn = 0
            continue

        g.current_card = players[turn].deck[play]
        time.sleep(1)  # pause
        if len(players[turn].deck) == 1:
            print(f"Player {turn+1} says UNO!")

        elif len(players[turn].deck) == 0:
            break

        players[turn].deck.remove(players[turn].deck[play])
        turn += 1
        if turn >= turns:
            turn = 0

    print(f"Player {turn+1} wins!")

    pass


if __name__ == "__main__":
    player_count = 4
    main(player_count)
