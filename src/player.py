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

        #Display Player Move Text
        display.player_move()

        #Get field from user input.
        field = input()

        #Column is A-J, row is 1-10.
        column = field.split('/')[0]
        row = field.split('/')[1]

        #Convert column and row to x and y coordinates.
        x = ord(column) - 65
        y = int(row) - 1

        self.board.set_hit(x, y)