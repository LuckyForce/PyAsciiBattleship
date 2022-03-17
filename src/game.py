#File Info:
#Created: 2020-01-27
#Author: Adrian Schauer
#Description: This file contains the main function of the game.

from enemy import Enemy
from player import Player
import display

class Game:
    def __init__(self, diff):
        "This function initializes the game."
        self.diff = diff
        self.ended = False
        self.enemy = Enemy(diff)
        self.player = Player()
    
    def setup(self):
        "This function sets up the game."
        print("Let's start with setting up the game!")
        while self.player.board.ships_placed != self.player.board.ships.__len__():
            self.player.place_ship()
            print("You have " + str(Player.ships_left) + " ships left to place.")
            self.player.board.print_ship_placements()

    def play(self):
        "This function plays the game."
        while self.ended == False:
            display.game_state(self)
            break
        