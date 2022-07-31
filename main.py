import random
import time

from game import Game
from player import Player


# Set conditions
# Condition 1: Same color
# Condition 2: Same number


def main():
    winner = False
    # Generate decks for each player
    p_o = Player()  # print(p_o.deck)
    p_t = Player()  # print(p_t.deck)

    players = [p_o, p_t]

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
        g.current_card = players[turn].deck[play]
        time.sleep(1)  # pause
        players[turn].deck.remove(players[turn].deck[play])
        print(players[turn].deck)
        turn += 1
        if turn == turns:
            turn = 0

    # Check game state
    for player in players:
        if len(player.deck) > 0:
            winner = False
        else:
            winner = True
            return player

    pass


if __name__ == "__main__":
    main()
