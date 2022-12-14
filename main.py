import random
import time

from game import Game
from player import Player, BotPlayer, NoobBotPlayer, ProBotPlayer
from cards import *


# Set conditions
# Condition 1: Same color
# Condition 2: Same number


def main(p_no, noob_bot_no, pro_bot_no):
    # Generate a game
    g = Game()
    # print(len(Game.pack))

    # Generate decks for each player
    global play
    players = []
    for i in range(p_no):
        players.append(Player())

    for i in range(noob_bot_no):
        players.append(NoobBotPlayer(g))

    for i in range(pro_bot_no):
        players.append(ProBotPlayer(g))


    # Play
    turns = len(players)
    turn = 0
    while True:
        if len(Game.pack) <= 0:
            g.prepare_pack()

        print(g.current_card)
        time.sleep(1)  # pause
        print(f"Player {turn+1}\'s turn.")
        print([i.value_as_dict for i in players[turn].deck])
        time.sleep(1)  # pause

        if isinstance(players[turn], BotPlayer):
            play = players[turn].play_turn()

        else:
            play = int(input(f"Enter a number from 0-{len(players[turn].deck)-1} \n"))

        time.sleep(1)  # pause
        if not players[turn].deck[play].check_color(g, players[turn].deck[play], players[turn].deck):
            Cards.draw(players[turn].deck)
            turn += 1
            if turn >= turns:
                turn = 0
            continue

        g.current_card = players[turn].deck[play].value_as_dict
        time.sleep(1)  # pause
        players[turn].deck.remove(players[turn].deck[play])

        if len(players[turn].deck) == 1:
            print(f"Player {turn+1} says UNO!")

        elif len(players[turn].deck) == 0:
            break

        turn += 1
        if turn >= turns:
            turn = 0

    print(f"Player {turn+1} wins!")

    pass


if __name__ == "__main__":
    player_count = 1
    noob_bot_count = 0
    pro_bot_count = 1
    main(player_count, noob_bot_count, pro_bot_count)
