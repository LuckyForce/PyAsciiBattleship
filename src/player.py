# File Info:
# Created: 2020-01-29
# Author: Adrian Schauer
# Description: This file contains class for player

from board import Board
import display


class Player:
    def __init__(self):
        self.moves = 0
        self.misses = 0
        self.board = Board()

    def make_move(self):
        self.moves += 1

        # Display Player Move Text
        display.player_move()

        # Get field from user input.
        field = input()

        #Column is A-J, row is 1-10.
        column = field.split('/')[0]
        row = field.split('/')[1]

        # Convert column and row to x and y coordinates.
        x = ord(column) - 65
        y = int(row) - 1

        # Check if field is valid.
        if self.board.move_invalid(x, y) == False:
            display.move_invalid()
        elif self.board.move_already_made(x, y) == True:
            display.move_already_made()
        else:
            hit = self.board.make_move(x, y)
            if hit == True:
                display.player_hit()
            else:
                display.player_miss()
                self.misses += 1
