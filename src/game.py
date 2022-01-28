#File Info:
#Created: 2020-01-27
#Author: Adrian Schauer
#Description: This file contains the main function of the game.

class Game:
    def __init__(self, diff):
        self.diff = diff
        self.moves = 0
        self.enemy_board = generate_board()
        self.player_board = generate_board()

    def play(self):
        pass

    def generate_board():
        return [10][10]
        