#File Info:
#Created: 2020-01-29
#Author: Adrian Schauer
#Description: This file contains class for player

from board import Board

class Player:
    def __init__(self):
        self.moves = 0
        self.board = Board()

    def make_move(self):
        self.moves += 1
        self.board.set_hit(x, y)