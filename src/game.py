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
        pass

    def play(self):
        "This function plays the game."
        while self.ended == False:
            display.game_state(self)
            break
        