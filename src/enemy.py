# File Info:
# Created: 2020-01-27
# Author: Adrian Schauer
# Description: This file contains the algorithm of the enemy AI.

import random
from board import Board


class Enemy:
    def __init__(self, diff):
        self.moves = 0
        self.misses = 0
        self.diff = diff
        self.board = Board()

    def generate_ship_placement(self):
        pass

    def make_move():
        pass

    def calculate_best_move(self):
        pass

    def calculate_random_move(self):
        pass

    def calculate_cheat_move(self):
        while True:
            # get random number between 0 and 9
            x = random.randint(0, 9)
            # get random number between 0 and 9
            y = random.randint(0, 9)
            # check if field has ship
            if self.board.get_field(x, y) == '.':
                return x, y

